#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from main.models import Book, BookClassification, LibraryUser, Guarantor, Loan
from main.forms import BookManageForm, BookClassificationManageForm, LibraryUserManageForm, GuarantorManageForm, LoanManageForm
import datetime, time
from main.forms import *

from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import inlineformset_factory

#@login_required(login_url='/login/')
def index(request):
	Loans = Loan.objects.all()
	c = {'Loans':Loans}
  	return render_to_response('loan/loans.html', c, context_instance=RequestContext(request))

#################################
##                             ##
##           Books             ##
##                             ##
#################################
def books_search(request):
   	# Default return list
   	Books = Book.objects.all()
   	results = []

	for book in Books:
   		libro = {'id':book.id, 'label':book.name, 'value':book.name}
   		results.append(libro)
   	return HttpResponse(simplejson.dumps(results),mimetype='application/json')

def xhr_test(request):
    if request.is_ajax():
        message = "Hello AJAX"
    else:
        message = "Hello"
    return HttpResponse(message)

def booksView(request):
	Books = Book.objects.all()
	c = {'Books':Books}
  	return render_to_response('book/books.html', c, context_instance=RequestContext(request))

def book_manageView(request, id = None, template_name='book/book_manage.html'):
	if id:
		bookI = get_object_or_404(Book, pk=id)
	else:
		bookI = Book()

	if request.method == 'POST':
		BookForm = BookManageForm(request.POST, request.FILES, instance=bookI)
		if BookForm.is_valid():
			BookForm.save()
			Books = Book.objects.all()
			c = {'Books':Books}
			return render_to_response('book/books.html', c, context_instance=RequestContext(request))
	else:
	 	BookForm = BookManageForm(instance=bookI)

	return render_to_response(template_name, {'BookForm': BookForm,}
			,context_instance = RequestContext(request))

#################################
##                             ##
##     Books Clasifications    ##
##                             ##
#################################

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

	return render_to_response(template_name, {'ClassificationForm': BookClassificationForm,}
			,context_instance = RequestContext(request))

def bookclassificationsView(request):
	BookClassifications = BookClassification.objects.all()
	c = {'Classifications':BookClassifications}
  	return render_to_response('classification/classifications.html', c, context_instance=RequestContext(request))

#################################
##                             ##
##   Books SubClasifications   ##
##                             ##
#################################

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

	return render_to_response(template_name, {'SubClassificationForm': BookSubClassificationForm,}
			,context_instance = RequestContext(request))

def booksubclassificationsView(request):
	BookSubClassifications = BookSubClassification.objects.all()
	c = {'SubClassifications':BookSubClassifications}
  	return render_to_response('subclassification/subclassifications.html', c, context_instance=RequestContext(request))

#################################
##                             ##
##            Users            ##
##                             ##
#################################

def usersView(request):
	Users = LibraryUser.objects.all()
	c = {'Users':Users}
  	return render_to_response('user/users.html', c, context_instance=RequestContext(request))

def delete_user(request, id = None):
	user = get_object_or_404(LibraryUser, pk=id)
	user.delete()
	
	Users = LibraryUser.objects.all()
	c = {'Users':Users}
  	return render_to_response('user/users.html', c, context_instance=RequestContext(request))
  	
def user_manageView(request, id = None, template_name='user/user_manage.html'):
	if id:
		userI = get_object_or_404(LibraryUser, pk=id)
	else:
		userI = LibraryUser()

	if request.method == 'POST':
		UserForm = LibraryUserManageForm(request.POST, request.FILES, instance=userI)
		if UserForm.is_valid():
			UserForm.save()
			Users = LibraryUser.objects.all()
			c = {'Users':Users}
			return render_to_response('user/users.html', c, context_instance=RequestContext(request))
	else:
	 	UserForm = LibraryUserManageForm(instance=userI)

	return render_to_response(template_name, {'UserForm': UserForm,}
			,context_instance = RequestContext(request))

#################################
##                             ##
##         Guarantor           ##
##                             ##
#################################

def guarantorsView(request):
	Guarantors = Guarantor.objects.all()
	c = {'Guarantors':Guarantors}
  	return render_to_response('guarantor/guarantors.html', c, context_instance=RequestContext(request))

def guarantor_manageView(request, id = None, template_name='guarantor/guarantor_manage.html'):
	if id:
		guarantorI = get_object_or_404(Guarantor, pk=id)
	else:
		guarantorI = Guarantor()

	if request.method == 'POST':
		GuarantorForm = GuarantorManageForm(request.POST, request.FILES, instance=guarantorI)
		if GuarantorForm.is_valid():
			GuarantorForm.save()
			Guarantors = Guarantor.objects.all()
			c = {'Guarantors':Guarantors}
			return render_to_response('guarantor/guarantors.html', c, context_instance=RequestContext(request))
	else:
	 	GuarantorForm = GuarantorManageForm(instance=guarantorI)

	return render_to_response(template_name, {'GuarantorForm': GuarantorForm,}
			,context_instance = RequestContext(request))

#################################
##                             ##
##           Loan              ##
##                             ##
#################################

def delete_loan(request, id = None):
	loan = get_object_or_404(Loan, pk=id)
	loan.delete()
	
	Loans = Loan.objects.all()
	c = {'Loans':Loans}
  	return render_to_response('loan/loans.html', c, context_instance=RequestContext(request))

def loansView(request):
	Loans = Loan.objects.all()
	c = {'Loans':Loans}
  	return render_to_response('loan/loans.html', c, context_instance=RequestContext(request))

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

			Loans = Loan.objects.all()
			c = {'Loans':Loans}

			return render_to_response(template_name, {'LoanForm': LoanForm, 'formset': formset}, context_instance=RequestContext(request))
	else:
	 	LoanForm = LoanManageForm(instance=loanI)
	 	formset = BookLoan_formset(instance=loanI)

	return render_to_response(template_name, {'LoanForm': LoanForm, 'formset': formset}, context_instance=RequestContext(request))

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