from django.views.generic.base import TemplateView

from rest_framework import viewsets
from .serializers import PlaylistSerializer
from .models import Playlist

class PlaylistPageView(TemplateView):
	template_name = 'playlists.html'

class PlaylistDetailPageView(TemplateView):
	template_name = 'playlist-detail.html'

class PlaylistDetailEditPageView(TemplateView):
	template_name = 'playlist-detail-edit.html'

class PlaylistViewSet(viewsets.ModelViewSet):
	model = Playlist
	serializer_class = PlaylistSerializer