from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from main.models import Book


#@login_required(login_url='/login/')
def index(request):
	Books = Book.objects.all()
	c = {'Books':Books}
  	return render_to_response('index.html', c, context_instance=RequestContext(request))
