from django.views.generic.base import TemplateView

class ProfilePageView(TemplateView):
	template_name = 'profile.html'

class ProfileEditPageView(TemplateView):
	template_name = 'profile-edit.html'