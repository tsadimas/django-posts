from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.list, name='list'),
	url(r'^(?P<postid>\d+)', views.detail,),
	url(r'^new/', views.post_form,name='post_new')
]
