from django.views.generic.base import TemplateView

class PlaylistPageView(TemplateView):
	template_name = 'playlists.html'

class PlaylistDetailPageView(TemplateView):
	template_name = 'playlist-detail.html'

class PlaylistDetailEditPageView(TemplateView):
	template_name = 'playlist-detail-edit.html'