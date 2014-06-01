from rest_framework import serializers
from .models import CountSongUser

class CountSongUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CountSongUser