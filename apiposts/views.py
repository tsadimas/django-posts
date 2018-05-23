import requests
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from posts.forms import PostsForm

#api_url = "http://localhost:3000"
api_url="https://node-test-197510.appspot.com"


def list(request):
    try:
        web_data = requests.get(url=api_url + "/todos",headers={"x-auth":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1YWE5MzI0M2E3YmZlYTJkN2U0ZjE0Y2IiLCJhY2Nlc3MiOiJhdXRoIiwiaWF0IjoxNTI0NjU3MzA2fQ.Kgu6xAfDBmQhMHi5AgvFNbQPc2zNV2zUJJT_cGPHV64"})
    except:
        context={'error': 'connection error'}
        return render(request, 'error.html', context)

    data = web_data.json()

    #for record in data:
    #    record["id"] = record.pop("_id")  # rename key _id (mongo) to id

    #context = {'data': data, 'url_redirect': 'apiposts'}
    context = {'data': data['todos']}
    print(data)
    print(type(data))

    #return render(request, 'api-list.html', context)
    return render(request, 'api-list.html', context)


def detail(request, postid):

    try:
        post = requests.get(url=api_url + "/posts/" + postid)
    except:
        context={'error': 'connection error'}
        return render(request, 'error.html', context)


    context = {'post': post.json()}
    return render(request, 'detail.html', context)


@login_required
def post_form(request):
    if request.method == 'GET':
        form = PostsForm()
    else:
        form = PostsForm(request.POST)

        if form.is_valid():
            data = {"title": form.cleaned_data['title'], "body": form.cleaned_data['body']}

            try:
                requests.post(api_url + "/posts", data=data)
            except:
                context = {'error': 'connection error'}
                return render(request, 'error.html', context)

            return HttpResponseRedirect("/apiposts/")

    return render(request, 'newpost.html', {'form': form, 'url_redirect': 'apiposts'})
