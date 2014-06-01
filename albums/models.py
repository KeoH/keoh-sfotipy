from django.db import models

from artists.models import Artist
from core.settings import MEDIA_URL as media

class Album(models.Model):

	title	= models.CharField(max_length=255)
	cover	= models.ImageField(upload_to='albums/', blank=True)
	artist 	= models.ForeignKey(Artist)

	def __unicode__(self):
		return self.title

	def get_cover(self):
		if(self.cover):
			return self.cover.url
		else:
			return ""


	def image_cover(self):
		html = '<figure><img width="60px" height="60px" src="%s"></figure>' % (self.cover.url)
		return html

	image_cover.allow_tags = True

class JamendoAlbum(models.Model):

	name	= models.CharField(max_length=255)
	cover   = models.URLField()
	release_date = models.DateField()
	artist_id_jamendo = models.PositiveIntegerField(default=1)
	artist_name = models.CharField(max_length=255)
	zip_file = models.URLField()

	def __unicode__(self):
		return self.name

