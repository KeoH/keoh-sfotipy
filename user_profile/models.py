from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):

	avatar = models.ImageField(upload_to='user_profile', default="")

	
