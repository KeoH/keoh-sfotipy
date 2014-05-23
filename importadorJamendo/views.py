from django.shortcuts import render

from django.views.generic.base import TemplateView

class ImportadorView(TemplateView):
	template_name = 'importador-artistas.html'