from django.db import models

from user_profile.models import UserProfile
from tracks.models import Track 

class CountSongUser(models.Model):

	count = models.PositiveIntegerField(default=1)
	user = models.ForeignKey(UserProfile)
	track = models.ForeignKey(Track)

	def __unicode__(self):
		text = "%s - usuario: %s" %(self.track.title, self.user.user.username)
		return text