import requests
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from posts.forms import PostsForm

def list(request):
    web_data = requests.get(url="http://localhost:3000/posts")
    data = web_data.json()

    for record in data:
        record["id"] = record.pop("_id") # rename key _id (mongo) to id

    context = {'data': data, 'url_redirect': 'apiposts'}
    return render(request, 'list.html', context)

def detail(request, postid):
	post = requests.get(url="http://localhost:3000/posts/"+postid)

	context = {'post': post.json()}
	return render(request, 'detail.html', context)

@login_required
def post_form(request):
	if request.method == 'GET':
		form = PostsForm()
	else:
		form = PostsForm(request.POST)

		if form.is_valid():
			data = { "title": form.cleaned_data['title'], "body": form.cleaned_data['body'] }

			requests.post("http://localhost:3000/posts", data= data)
			return HttpResponseRedirect("/apiposts/")

	return render(request, 'newpost.html', {'form': form, 'url_redirect': 'apiposts'})
