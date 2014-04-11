from django.views.generic.base import TemplateView

class ArtistDetailPageView(TemplateView):
	template_name = 'artist-detail.html'