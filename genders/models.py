from django.db import models

from albums.models import Album
from artists.models import Artist
from tracks.models import Track

class Gender(models.Model):

	name = models.CharField(max_length=255)

	album = models.ManyToManyField(Album,related_name='+', blank=True)
	artist = models.ManyToManyField(Artist,related_name='+', blank=True)
	track = models.ManyToManyField(Track,related_name='+', blank=True)

	def __unicode__(self):
		return self.name

	def how_many_albums(self):
		number = self.album.count()
		return number	

	def how_many_artists(self):
		number = self.artist.count()
		return number	

	def how_many_tracks(self):
		number = self.track.count()
		return number