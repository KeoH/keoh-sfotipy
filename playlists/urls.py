#encoding:utf-8
from django.conf.urls import patterns, url
from .views import PlaylistPageView, PlaylistDetailPageView, PlaylistDetailEditPageView

urlpatterns = patterns('',
	url(r'^$', PlaylistPageView.as_view(), name='home'),
	url(r'^detail/$', PlaylistDetailPageView.as_view(), name='detail'),
	url(r'^edit/$', PlaylistDetailEditPageView.as_view(), name='edit'),
)