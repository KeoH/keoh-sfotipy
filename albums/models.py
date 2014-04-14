from django.db import models

from artists.models import Artist
from core.settings import MEDIA_URL as media

class Album(models.Model):

	title	= models.CharField(max_length=255)
	cover	= models.ImageField(upload_to='albums/', blank=True)
	artist 	= models.ForeignKey(Artist)

	def __unicode__(self):
		return self.title

	def image_cover(self):
		html = '<figure><img width="60px" height="60px" src="%s"></figure>' % (self.cover.url)
		return html

	image_cover.allow_tags = True