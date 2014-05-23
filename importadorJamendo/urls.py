#encoding:utf-8
from django.conf.urls import patterns, url
from .views import ImportadorView

urlpatterns = patterns('',
	url(r'^$', ImportadorView.as_view(), name='home'),
)