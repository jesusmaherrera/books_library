from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from main.models import Book, BookClassification, LibraryUser, Guarantor
from main.forms import BookManageForm, BookClassificationManageForm, LibraryUserManageForm, GuarantorManageForm

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