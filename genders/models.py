from django.db import models

from albums.models import Album
from artists.models import Artist

class Gender(models.Model):

	name = models.CharField(max_length=255)

	albun = models.ManyToManyField(Album,related_name='+', blank=True)
	artist = models.ManyToManyField(Artist,related_name='+', blank=True)

	def __unicode__(self):
		return self.name