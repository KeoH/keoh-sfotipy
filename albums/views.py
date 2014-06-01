from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .serializers import AlbumSerializer
from .models import Album

class AlbumDetailPageView(TemplateView):
	template_name = 'album-detail.html'

class AlbumViewSet(viewsets.ModelViewSet):
	model = Album
	serializer_class = AlbumSerializer