from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView

from artists.models import Artist
from tracks.models import Track
from user_profile.forms import EmailUserCreationForm

class HomePageView(View):
	def get(self, request):

		if request.user.is_authenticated():
			template_name = 'home.html'
			return render(request, template_name)
		else:
			template_name = 'home-without-auth.html'
			form_usercreation = EmailUserCreationForm()
			return render(request, template_name, {'form_singup': form_usercreation})

	def post(self, request):

		if not request.user.is_authenticated():
			template_name = 'home-without-auth.html'
			form_usercreation = EmailUserCreationForm(request.POST or None)

			if form_usercreation.is_valid():
				form_usercreation.save()
				return HttpResponseRedirect(reverse('profile:success'))		
			
			return render(request, template_name, {'form_singup': form_usercreation})


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