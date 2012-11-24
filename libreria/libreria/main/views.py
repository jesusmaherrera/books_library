#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from libreria.main.models import Book, BookClassification, LibraryUser, Guarantor, Loan
from libreria.main.forms import BookManageForm, BookClassificationManageForm, LibraryUserManageForm, GuarantorManageForm, LoanManageForm
import datetime, time
from libreria.main.forms import *
from django.db.models import Q

from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import inlineformset_factory

#Paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# user autentication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required

##########################################
## 										##
##               LOGIN     			    ##
##										##
##########################################
#userI = get_object_or_404(User, pk=1)
#	userI.set_password('nov12admin')
#	userI.save()
def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('login.html',{'form':formulario, 'message':'Nombre de usaurio o password no validos',}, context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('login.html',{'form':formulario, 'message':'',}, context_instance=RequestContext(request))

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def users(request, template="registration/users.html"):
   users = User.objects.all()
   c = {'users':users}
   return render_to_response(template, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')  	
def appuser_manageView(request, id = None, template_name='registration/user_manage.html'):
	if id:
		userI = get_object_or_404(User, pk=id)
	else:
		userI = User()

	if request.method == 'POST':
		UserForm = AdminPasswordChangeForm(request.POST, request.FILES, instance=userI)
		if UserForm.is_valid():
			UserForm.save()
			return HttpResponseRedirect('/appusers/')
	else:
	 	UserForm = UserCreationForm(instance=userI)

	return render_to_response(template_name, {'UserForm': UserForm,}
			,context_instance = RequestContext(request))

@login_required(login_url='/login/')
def index(request):
	Loans = Loan.objects.all()
	c = {'Loans':Loans}
  	return render_to_response('loan/loans.html', c, context_instance=RequestContext(request))

#################################
##                             ##
##           Books             ##
##                             ##
#################################
@login_required(login_url='/login/')
def books_search(request):
   	# Default return list
   	Books = Book.objects.all()
   	results = []

	for book in Books:
   		libro = {'id':book.id, 'label':book.name, 'value':book.name}
   		results.append(libro)
   	return HttpResponse(simplejson.dumps(results),mimetype='application/json')

@login_required(login_url='/login/')
def xhr_test(request):
    if request.is_ajax():
        message = "Hello AJAX"
    else:
        message = "Hello"
    return HttpResponse(message)

@login_required(login_url='/login/')
def booksView(request):
	filtro = request.GET['filtro']

	book_list = Book.objects.filter(Q(name__icontains=filtro) | Q(autor__icontains=filtro) | Q(editorial__icontains=filtro)| Q(book_classification__name__icontains=filtro) | Q(book_subclassification__name__icontains=filtro))
	paginator = Paginator(book_list, 10) # Show 25 contacts per page
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    books = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    books = paginator.page(paginator.num_pages)
	c = {'Books':books,'filtro':filtro}
	return render_to_response('book/books.html', c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete_book(request, id = None):
	book = get_object_or_404(Book, pk=id)
	book.delete()
	
	return HttpResponseRedirect('/books/?filtro=')

@login_required(login_url='/login/')
def book_manageView(request, id = None, template_name='book/book_manage.html'):
	if id:
		bookI = get_object_or_404(Book, pk=id)
	else:
		bookI = Book()

	if request.method == 'POST':
		BookForm = BookManageForm(request.POST, request.FILES, instance=bookI)
		if BookForm.is_valid():
			BookForm.save()
			return HttpResponseRedirect('/books/?filtro=')
	else:
	 	BookForm = BookManageForm(instance=bookI)

	return render_to_response(template_name, {'BookForm': BookForm,}
			,context_instance = RequestContext(request))

#################################
##                             ##
##     Books Clasifications    ##
##                             ##
#################################

@login_required(login_url='/login/')
def  bookclassification_manageView(request, id = None, template_name='classification/classification_manage.html'):
	if id:
		bookclassificationI = get_object_or_404(BookClassification, pk=id)
	else:
		bookclassificationI =  BookClassification()

	if request.method == 'POST':
		BookClassificationForm = BookClassificationManageForm(request.POST, request.FILES, instance=bookclassificationI)
		if BookClassificationForm.is_valid():
			BookClassificationForm.save()
			BookClassifications = BookClassification.objects.all()
			c = {'Classifications':BookClassifications}
			return render_to_response('classification/classifications.html', c, context_instance=RequestContext(request))
	else:
	 	BookClassificationForm = BookClassificationManageForm(instance=bookclassificationI)

	return render_to_response(template_name, {'ClassificationForm': BookClassificationForm,'id':id}
			,context_instance = RequestContext(request))

@login_required(login_url='/login/')
def bookclassificationsView(request):
	filtro = request.GET['filtro']

	BookClassifications = BookClassification.objects.filter(name__icontains=filtro)
	c = {'Classifications':BookClassifications,'filtro':filtro}
  	return render_to_response('classification/classifications.html', c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete_bookclassification(request, id = None):
	bookClassification = get_object_or_404(BookClassification, pk=id)
	bookClassification.delete()
	
	BookClassifications = BookClassification.objects.all()
	c = {'Classifications':BookClassifications}
  	return render_to_response('classification/classifications.html', c, context_instance=RequestContext(request))

#################################
##                             ##
##   Books SubClasifications   ##
##                             ##
#################################
@login_required(login_url='/login/')
def  booksubclassification_manageView(request, id = None, template_name='subclassification/subclassification_manage.html'):
	if id:
		booksubclassificationI = get_object_or_404(BookSubClassification, pk=id)
	else:
		booksubclassificationI =  BookSubClassification()

	if request.method == 'POST':
		BookSubClassificationForm = BookSubClassificationManageForm(request.POST, request.FILES, instance=booksubclassificationI)
		if BookSubClassificationForm.is_valid():
			BookSubClassificationForm.save()
			BookSubClassifications = BookSubClassification.objects.all()
			c = {'SubClassifications':BookSubClassifications}
			return render_to_response('subclassification/subclassifications.html', c, context_instance=RequestContext(request))
	else:
	 	BookSubClassificationForm = BookSubClassificationManageForm(instance=booksubclassificationI)

	return render_to_response(template_name, {'SubClassificationForm': BookSubClassificationForm,'id':id}
			,context_instance = RequestContext(request))

@login_required(login_url='/login/')
def booksubclassificationsView(request):
	filtro = request.GET['filtro']
	BookSubClassifications = BookSubClassification.objects.filter(
		Q(name__icontains=filtro)| Q(book_clasification__name__icontains=filtro)
		)
	c = {'SubClassifications':BookSubClassifications,'filtro':filtro}
  	return render_to_response('subclassification/subclassifications.html', c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete_booksubclassification(request, id = None):
	bookSubClassification = get_object_or_404(BookSubClassification, pk=id)
	bookSubClassification.delete()
	
	BookSubClassifications = BookSubClassification.objects.all()
	c = {'SubClassifications':BookSubClassifications}
  	return render_to_response('subclassification/subclassifications.html', c, context_instance=RequestContext(request))
#################################
##                             ##
##            Users            ##
##                             ##
#################################
@login_required(login_url='/login/')
def usersView(request):
	filtro = request.GET['filtro']
	user_list = LibraryUser.objects.filter(
		Q(name__icontains=filtro)| Q(guarantor__name__icontains=filtro)
		)

	paginator = Paginator(user_list, 10) # Show 25 contacts per page
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    users = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    users = paginator.page(paginator.num_pages)


	c = {'Users':users,'filtro':filtro}
  	return render_to_response('user/users.html', c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete_user(request, id = None):
	user = get_object_or_404(LibraryUser, pk=id)
	user.delete()
	
	return HttpResponseRedirect('/users/?filtro=')

@login_required(login_url='/login/')  	
def user_manageView(request, id = None, template_name='user/user_manage.html'):
	if id:
		userI = get_object_or_404(LibraryUser, pk=id)
	else:
		userI = LibraryUser()

	if request.method == 'POST':
		UserForm = LibraryUserManageForm(request.POST, request.FILES, instance=userI)
		if UserForm.is_valid():
			UserForm.save()
			return HttpResponseRedirect('/users/?filtro=')
	else:
	 	UserForm = LibraryUserManageForm(instance=userI)

	return render_to_response(template_name, {'UserForm': UserForm,}
			,context_instance = RequestContext(request))

#################################
##                             ##
##         Guarantor           ##
##                             ##
#################################
@login_required(login_url='/login/')
def guarantorsView(request):
	filtro = request.GET['filtro']

	guarantor_list = Guarantor.objects.filter(name__icontains=filtro)
	paginator = Paginator(guarantor_list, 10) # Show 25 contacts per page
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		guarantors = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    guarantors = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    guarantors = paginator.page(paginator.num_pages)


	c = {'Guarantors':guarantors,'filtro':filtro}
  	return render_to_response('guarantor/guarantors.html', c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete_guarantor(request, id = None):
	guarantor = get_object_or_404(Guarantor, pk=id)
	guarantor.delete()
	
	return HttpResponseRedirect('/guarantors/?filtro=')

@login_required(login_url='/login/')
def guarantor_manageView(request, id = None, template_name='guarantor/guarantor_manage.html'):
	if id:
		guarantorI = get_object_or_404(Guarantor, pk=id)
	else:
		guarantorI = Guarantor()

	if request.method == 'POST':
		GuarantorForm = GuarantorManageForm(request.POST, request.FILES, instance=guarantorI)
		if GuarantorForm.is_valid():
			GuarantorForm.save()
			return HttpResponseRedirect('/guarantors/?filtro=')
	else:
	 	GuarantorForm = GuarantorManageForm(instance=guarantorI)

	return render_to_response(template_name, {'GuarantorForm': GuarantorForm,}
			,context_instance = RequestContext(request))

#################################
##                             ##
##           Loan              ##
##                             ##
#################################
@login_required(login_url='/login/')
def delete_loan(request, id = None):
	loan = get_object_or_404(Loan, pk=id)
	loan.delete()
	
	return HttpResponseRedirect('/loans/?start=')

@login_required(login_url='/login/')
def loansView(request):
	if request.GET['start'] !='':
		fechaInicio = request.GET['start']
		fechaFin = request.GET['end']
	else:
		fechaInicio=datetime.now().strftime("%Y-%m-01"+" %H:%M")
		fechaFin =datetime.now().strftime("%Y-%m-%d %H:%M")

	loan_list = Loan.objects.filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin)
	paginator = Paginator(loan_list, 10) # Show 25 contacts per page
	page = request.GET.get('page')

	#####PARA PAGINACION##############
	try:
		loans = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    loans = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    loans = paginator.page(paginator.num_pages)


	c = {'Loans':loans,'fechaInicio':fechaInicio,'fechaFin':fechaFin}
  	return render_to_response('loan/loans.html', c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def loan_manage_inlineView(request, id = None, template_name='loan/loan_manage_inline.html'):
	BookLoan_formset = get_bookloan_items_formset(BookLoanManageForm, extra=1, can_delete=True)

	if id:
		loanI = get_object_or_404(Loan, pk=id)
	else:
		loanI = Loan()

	if request.method == 'POST':

		LoanForm = LoanManageForm(request.POST, request.FILES, instance=loanI)
		formset = BookLoan_formset(request.POST, request.FILES, instance=loanI)
		if LoanForm.is_valid() and formset.is_valid():
			LoanForm.save()
			formset.save()

			return HttpResponseRedirect('/loans/?start=')
	else:
	 	LoanForm = LoanManageForm(instance=loanI)
	 	formset = BookLoan_formset(instance=loanI)

	return render_to_response(template_name, {'LoanForm': LoanForm, 'formset': formset}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def loansReportView(request, template_name='loan/loansReport.html'):
	if request.GET['start'] !='':
		fechaInicio = request.GET['start']
		fechaFin = request.GET['end']
	else:
		fechaInicio=datetime.now().strftime("%Y-%m-01"+" %H:%M")
		fechaFin =datetime.now().strftime("%Y-%m-%d %H:%M")

	if request.GET['_btn'] == 'Imprimir Reporte':
			template_name='loan/loansReportR.html'

	fechaInicioO = datetime.strptime(fechaInicio, '%Y-%m-%d %H:%M')	

	mayores = Loan.objects.filter(user__age__gte=60).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	adultos = Loan.objects.filter(user__age__lt=60).filter(user__age__gte=19).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	jovenes = Loan.objects.filter(user__age__lt=19).filter(user__age__gte=13).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	ninos = Loan.objects.filter(user__age__lt=13).filter(user__age__gte=6).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	preescolar = Loan.objects.filter(user__age__lt=6).filter(user__age__gte=3).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()

	consulta = BookLoan.objects.filter(book__book_classification__name='CONSULTA').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	general = BookLoan.objects.filter(book__book_classification__name='GENERAL').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	debilesvisuales = BookLoan.objects.filter(book__book_classification__name='MATERIAL PARA DÉBILES VISUALES E INVIDENTES ').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	infantil = BookLoan.objects.filter(book__book_classification__name='INFANTIL').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	audiovisual = BookLoan.objects.filter(book__book_classification__name='MATERIAL AUDIO VISUAL').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	now = datetime.now()
	c = {'mayores':mayores,'adultos':adultos,'jovenes':jovenes,'ninos':ninos,'preescolar':preescolar,'consulta':consulta,'general': general, 'debilesvisuales':debilesvisuales,'infantil':infantil,'audiovisual':audiovisual,'fechaActual':now.strftime("%d/%m/%Y a las %H:%M:%S"),'fechaInicio':fechaInicio,'fechaFin':fechaFin,'fechaInicioO':fechaInicioO}
  	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def generalloansReportView(request, template_name='loan/general_loansReport.html'):
	if request.GET['start'] !='':
		fechaInicio = request.GET['start']
		fechaFin = request.GET['end']
	else:
		fechaInicio=datetime.now().strftime("%Y-%m-01"+" %H:%M")
		fechaFin =datetime.now().strftime("%Y-%m-%d %H:%M")

	if request.GET['_btn'] == 'Imprimir Reporte':
			template_name='loan/loansReportR.html'

	fechaInicioO = datetime.strptime(fechaInicio, '%Y-%m-%d %H:%M')	

	libros = Loan.objects.filter(loan_type="L").filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	librosDomicilio = Loan.objects.filter(loan_type="LD").filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	internet = Loan.objects.filter(loan_type="C").filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	now = datetime.now()
	c = {'fechaInicio':fechaInicio,'fechaFin':fechaFin,'fechaInicioO':fechaInicioO,'libros':libros,'librosDomicilio':librosDomicilio,'internet':internet}
  	return render_to_response(template_name, c, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def loansReportRView(request, template_name='loan/loansReportR.html'):
	if request.GET['start'] !='':
		fechaInicio = request.GET['start']
		fechaFin = request.GET['end']
	else:
		fechaInicio=datetime.now().strftime("%Y-%m-01"+" %H:%M")
		fechaFin =datetime.now().strftime("%Y-%m-%d %H:%M")

	mayores = Loan.objects.filter(user__age__gte=60).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	adultos = Loan.objects.filter(user__age__lt=60).filter(user__age__gte=19).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	jovenes = Loan.objects.filter(user__age__lt=19).filter(user__age__gte=13).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	ninos = Loan.objects.filter(user__age__lt=13).filter(user__age__gte=6).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()
	preescolar = Loan.objects.filter(user__age__lt=6).filter(user__age__gte=3).filter(loan_date__gt=fechaInicio).filter(loan_date__lte=fechaFin).count()

	consulta = BookLoan.objects.filter(book__book_classification__name='CONSULTA').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	general = BookLoan.objects.filter(book__book_classification__name='GENERAL').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	debilesvisuales = BookLoan.objects.filter(book__book_classification__name='MATERIAL PARA DÉBILES VISUALES E INVIDENTES ').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	infantil = BookLoan.objects.filter(book__book_classification__name='INFANTIL').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	audiovisual = BookLoan.objects.filter(book__book_classification__name='MATERIAL AUDIO VISUAL').filter(loan__loan_date__gt=fechaInicio).filter(loan__loan_date__lte=fechaFin).count()
	now = datetime.now()
	c = {'mayores':mayores,'adultos':adultos,'jovenes':jovenes,'ninos':ninos,'preescolar':preescolar,'consulta':consulta,'general': general, 'debilesvisuales':debilesvisuales,'infantil':infantil,'audiovisual':audiovisual,'fechaActual':now.strftime("%d/%m/%Y a las %H:%M:%S"),'fechaInicio':fechaInicio,'fechaFin':fechaFin}
  	return render_to_response(template_name, c, context_instance=RequestContext(request))
