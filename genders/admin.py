from django.contrib import admin

from .models import Gender

class GendersAdmin(admin.ModelAdmin):
	list_display = ('name', 'how_many_tracks','how_many_artists','how_many_albums')

admin.site.register(Gender, GendersAdmin)