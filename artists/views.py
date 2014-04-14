from django.views.generic import DetailView

# class ArtistDetailPageView(TemplateView):
# 	template_name = 'artist-detail.html'

from .models import Artist
from albums.models import Album
from tracks.models import Track

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