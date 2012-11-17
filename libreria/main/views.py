#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from main.models import Book, BookClassification, LibraryUser, Guarantor, Loan
from main.forms import BookManageForm, BookClassificationManageForm, LibraryUserManageForm, GuarantorManageForm, LoanManageForm
from main.forms import *

from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import inlineformset_factory

#@login_required(login_url='/login/')
def index(request):
	Books = Book.objects.all()
	c = {'Books':Books}
  	return render_to_response('index.html', c, context_instance=RequestContext(request))

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

def loansReportView(request):
	mayores = Loan.objects.filter(user__age__gte=60).count()
	adultos = Loan.objects.filter(user__age__lt=60).filter(user__age__gte=19).count()
	jovenes = Loan.objects.filter(user__age__lt=19).filter(user__age__gte=13).count()
	ninos = Loan.objects.filter(user__age__lt=13).filter(user__age__gte=6).count()
	preescolar = Loan.objects.filter(user__age__lt=6).filter(user__age__gte=3).count()

	consulta = BookLoan.objects.filter(book__book_classification__name='CONSULTA').count()
	general = BookLoan.objects.filter(book__book_classification__name='GENERAL').count()
	debilesvisuales = BookLoan.objects.filter(book__book_classification__name='MATERIAL PARA DÉBILES VISUALES E INVIDENTES ').count()
	infantil = BookLoan.objects.filter(book__book_classification__name='INFANTIL').count()
	audiovisual = BookLoan.objects.filter(book__book_classification__name='MATERIAL AUDIO VISUAL').count()
	
	

	c = {'mayores':mayores,'adultos':adultos,'jovenes':jovenes,'ninos':ninos,'preescolar':preescolar,'consulta':consulta,'general': general, 'debilesvisuales':debilesvisuales,'infantil':infantil,'audiovisual':audiovisual}
  	return render_to_response('loan/loansReport.html', c, context_instance=RequestContext(request))