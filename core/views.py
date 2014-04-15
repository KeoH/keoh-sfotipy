from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView

from artists.models import Artist
from tracks.models import Track

class HomePageView(View):
	def get(self, request):
		if request.user.is_authenticated():
			template_name = 'home.html'
		else:
			template_name = 'home-without-auth.html'
		return render(request, template_name)


class PlayingPageView(TemplateView):
	template_name = 'playing.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PlayingPageView, self).dispatch(*args, **kwargs)


class TopHitsView(ListView):
	context_object_name = 'tracks'
	template_name = 'top_hits.html'
	queryset = Track.objects.all()

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TopHitsView, self).dispatch(*args, **kwargs)


class SearchPageView(TemplateView):
	template_name = 'search.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SearchPageView, self).dispatch(*args, **kwargs)