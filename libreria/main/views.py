from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from main.models import Book, BookClassification
from main.forms import BookManageForm, BookClassificationManageForm

#@login_required(login_url='/login/')
def index(request):
	Books = Book.objects.all()
	c = {'Books':Books}
  	return render_to_response('index.html', c, context_instance=RequestContext(request))

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