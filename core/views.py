from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
	template_name = 'home.html'

class PlayingPageView(TemplateView):
	template_name = 'playing.html'

class TopHitsPageView(TemplateView):
	template_name = 'top_hits.html'

class SearchPageView(TemplateView):
	template_name = 'search.html'