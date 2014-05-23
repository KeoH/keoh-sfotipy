from django.contrib import admin

from artists.models import JamendoArtist
from albums.models import JamendoAlbum
from tracks.models import JamendoTrack

admin.site.register(JamendoArtist)
admin.site.register(JamendoAlbum)
admin.site.register(JamendoTrack)
