from django.shortcuts import render_to_response
from django.http import Http404
# Create your views here.
from sblog.models import Blog

def blog_list(request):
	blogs=Blog.objects.all()
	return render_to_response("blog_list.html",{"blogs":blogs})

def blog_show(request,id=''):
	try:
		blog=Blog.objects.get(id=id)
	except Blog.DoesNotExist:
		raise Http404
	return render_to_response("blog_show.html",{"blog":blog})