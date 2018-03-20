from django.shortcuts import render

# Create your views here.
from .models import Posts

def list(request):
	data = Posts.objects.all()
	context = {'data' : data}
	return render(request, 'list.html', context)

def detail(request, postid):
	post = Posts.objects.get(pk=postid)
	context = {'post': post}
	return render(request, 'detail.html', context)
