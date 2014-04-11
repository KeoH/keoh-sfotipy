from django.views.generic.base import TemplateView
from django.views.generic import ListView

from artists.models import Artist
from tracks.models import Track

class HomePageView(TemplateView):
	template_name = 'home.html'

class PlayingPageView(TemplateView):
	template_name = 'playing.html'

class TopHitsView(ListView):
	context_object_name = 'tracks'
	template_name = 'top_hits.html'
	queryset = Track.objects.all()


class SearchPageView(TemplateView):
	template_name = 'search.html'