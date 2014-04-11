from django.conf.urls import patterns, include, url

from core.views import HomePageView, PlayingPageView, TopHitsView, SearchPageView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home' ),
    url(r'^playing/$', PlayingPageView.as_view(), name='playing' ),
    url(r'^tophits/$', TopHitsView.as_view(), name='tophits' ),
    url(r'^search/$', SearchPageView.as_view(), name='search' ),

    url(r'^artists/', include('artists.urls')),
    url(r'^albums/', include('albums.urls')),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^playlist/', include('playlists.urls')),

)
