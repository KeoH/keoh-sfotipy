from django.views.generic import DetailView

from .models import Artist, Country
from albums.models import Album
from tracks.models import Track

from rest_framework import viewsets
from .serializers import CountrySerializer, ArtistSerializer

class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'artist'
	template_name = 'artist-detail.html'

	def get_context_data(self, **kwargs):
		context = super(ArtistDetailView, self).get_context_data(**kwargs)
		artist = kwargs['object'] 
		context['tophits'] = Track.objects.filter(artist=artist.pk)[:3]
		context['albums'] = Album.objects.filter(artist=artist.pk)
		return context


class CountryViewSet(viewsets.ModelViewSet):
	model = Country
	serializer_class = CountrySerializer

class ArtistViewSet(viewsets.ModelViewSet):
	model = Artist
	serializer_class = ArtistSerializer