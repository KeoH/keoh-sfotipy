from django.db import models

from albums.models import Album, JamendoAlbum
from artists.models import Artist, JamendoArtist

from core.settings import STATIC_URL as media

class Track(models.Model):

	title		= models.CharField(max_length=255)
	order		= models.PositiveIntegerField(default=1)
	track_field	= models.FileField(upload_to='tracks')
	album		= models.ForeignKey(Album)
	artist		= models.ForeignKey(Artist)
	duration    = models.PositiveIntegerField(default=1)

	def __unicode__(self):
		return self.title

	def audio_track(self):
		html = '<audio controls preload="none"><source src="%s" type="audio/mpeg"></audio>' % (self.track_field.url)	
		return html

	audio_track.allow_tags = True

class JamendoTrack(models.Model):

	id_jamendo = models.PositiveIntegerField(default=1)
	order = models.PositiveIntegerField(default=1)
	title = models.CharField(max_length=255)
	duration = models.PositiveIntegerField(default=1)
	audio = models.URLField()
	audiodownload = models.URLField()
	album = models.ForeignKey(JamendoAlbum)
	artist = models.ForeignKey(JamendoArtist)

	def __unicode__(self):
		return self.title