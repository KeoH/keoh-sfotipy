from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('title','artist','album','audio_track')
	ordering = ('title',)

admin.site.register(Track, TrackAdmin)