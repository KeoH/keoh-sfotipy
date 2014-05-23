from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View, DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout

from artists.models import Artist
from albums.models import Album
from tracks.models import Track
from user_profile.forms import EmailUserCreationForm, UserLoginForm

class HomePageView(View):
	def get(self, request):

		if request.user.is_authenticated():
			template_name = 'home.html'
			return render(request, template_name)
		else:
			template_name = 'home-without-auth.html'
			form_usercreation = EmailUserCreationForm()
			form_userlogin = UserLoginForm()
			return render(request, template_name, {'form_signup': form_usercreation, 'form_signin': form_userlogin})

	def post(self, request):

		if not request.user.is_authenticated():
			template_name = 'home-without-auth.html'
			form_usercreation = EmailUserCreationForm(request.POST or None)
			form_userlogin = UserLoginForm(request.POST or None)

			if form_usercreation.is_valid():
				form_usercreation.save()
				return HttpResponseRedirect(reverse('home'))		

			if form_userlogin.is_valid():
				login(request, form_userlogin.get_user())
			return HttpResponseRedirect(reverse('home'))
			
			return render(request, template_name, {'form_signup': form_usercreation})

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('home'))


class PlayingPageView(DetailView):
	model = Track
	context_object_name = 'track'
	template_name = 'playing.html'

	def get_context_data(self, **kwargs):
		context = super(PlayingPageView, self).get_context_data(**kwargs)
		track = kwargs['object'] 
		context['pistas'] = Track.objects.filter(album=track.album.pk).order_by('order')
		return context


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

# Vistas para el manejo de errores 404, 403 y 500

def error404(request):
	return render(request, 'error404.html')

def error500(request):
	return render(request, 'error500.html')

def error403(request):
	return render(request, 'error403.html')