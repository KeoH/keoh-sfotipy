from django.db import models

from albums.models import Album
from artists.models import Artist

from core.settings import MEDIA_URL as media

class Track(models.Model):

	title		= models.CharField(max_length=255)
	order		= models.PositiveIntegerField(default=1)
	track_field	= models.FileField(upload_to='tracks')
	album		= models.ForeignKey(Album)
	artist		= models.ForeignKey(Artist)

	def __unicode__(self):
		return self.title

	def audio_track(self):
		html = '<audio controls preload="none"><source src="%s%s" type="audio/mpeg"></audio>' % (media, self.track_field)	
		return html

	audio_track.allow_tags = True