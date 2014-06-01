from albums.views import AlbumViewSet
from artists.views import CountryViewSet, ArtistViewSet
from core.views import HomePageView, PlayingPageView, TopHitsView, LogoutView, SearchPageView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from genders.views import GenderViewSet
from playlists.views import PlaylistViewSet
from rest_framework import routers
from rest_framework import viewsets, serializers
from tracks.views import TrackViewSet
from user_profile.models import UserProfile
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        depth = 1

class UserProfileViewSet(viewsets.ModelViewSet):
    model = UserProfile
    serializer_class = UserProfileSerializer

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'genders', GenderViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'userprofile', UserProfileViewSet)
router.register(r'playlists', PlaylistViewSet)



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
    url(r'^api/', include(router.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.error404'
handler403 = 'core.views.error403'
handler500 = 'core.views.error500'

