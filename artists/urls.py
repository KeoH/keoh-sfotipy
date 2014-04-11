#encoding:utf-8
from django.conf.urls import patterns, url
from .views import ArtistDetailPageView

urlpatterns = patterns('',
	url(r'^$', ArtistDetailPageView.as_view(), name='detail'),
)