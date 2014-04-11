from django.db import models

from albums.models import Album
from artists.models import Artist

class Gender(models.Model):

	name = models.CharField(max_length=255)

	albun = models.ForeignKey(Album)
	artist = models.ForeignKey(Artist)