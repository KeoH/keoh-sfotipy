from django.contrib import admin

from .models import Album

class AlbumAdmin(admin.ModelAdmin):
	ordering = ('title',)
	list_display = ('title', 'artist', 'image_cover')

admin.site.register(Album, AlbumAdmin)