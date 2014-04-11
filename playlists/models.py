from django.db import models

from tracks.models import Track
from user_profile.models import UserProfile 

class Playlist(models.Model):

	name = models.CharField(max_length=255)

	tracks = models.ManyToManyField(Track, blank=True)
	owner = models.ForeignKey(UserProfile,related_name='+')
	followers = models.ManyToManyField(UserProfile,related_name='+', blank=True)

	def __unicode__(self):
		return self.name + " - by:" + self.owner.username