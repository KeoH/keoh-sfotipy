from django.conf.urls import patterns, include, url

from core.views import HomePageView, PlayingPageView, TopHitsView, LogoutView, SearchPageView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home' ),
    url(r'^playing/(?P<pk>[-_\w]+)/$', PlayingPageView.as_view(), name='playing' ),
    url(r'^tophits/$', TopHitsView.as_view(), name='tophits' ),
    url(r'^search/$', SearchPageView.as_view(), name='search' ),

    url(r'^logout/$', LogoutView.as_view(), name='logout' ),

    url(r'^artists/', include('artists.urls', namespace='artist')),
    url(r'^albums/', include('albums.urls', namespace='album')),
    url(r'^playlist/', include('playlists.urls', namespace='playlist')),

    url(r'^importador/', include('importadorJamendo.urls', namespace='importador')),
)

handler404 = 'core.views.error404'
handler403 = 'core.views.error403'
handler500 = 'core.views.error500'
