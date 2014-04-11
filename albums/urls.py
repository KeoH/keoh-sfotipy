#encoding:utf-8
from django.conf.urls import patterns, url
from .views import AlbumDetailPageView

urlpatterns = patterns('',
	url(r'^$', AlbumDetailPageView.as_view(), name='detail'),
)