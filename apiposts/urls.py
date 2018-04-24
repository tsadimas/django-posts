from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.list),
	url(r'^new/', views.post_form),
	url(r'^(?P<postid>\w+)', views.detail),
]
