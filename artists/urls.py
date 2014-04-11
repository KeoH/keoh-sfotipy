#encoding:utf-8
from django.conf.urls import patterns, url
from .views import ArtistDetailView

urlpatterns = patterns('',
	url(r'^(?P<pk>[-_\w]+)/$', ArtistDetailView.as_view(), name='detail'),
)