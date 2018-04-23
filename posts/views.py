from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Posts
from .forms import PostsForm

def list(request):
	data = Posts.objects.all()
	context = {'data' : data}
	return render(request, 'list.html', context)

def detail(request, postid):
	post = Posts.objects.get(pk=postid)
	context = {'post': post}
	return render(request, 'detail.html', context)

@login_required
def post_form(request):
	if request.method == 'GET':
		form = PostsForm()
	else:
		form = PostsForm(request.POST)

		if form.is_valid():
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			post = Posts.objects.create(title=title,body=body,userId = request.user)
			return HttpResponseRedirect("/posts/"+str(post.id))

	return render(request, 'newpost.html', {'form': form})
