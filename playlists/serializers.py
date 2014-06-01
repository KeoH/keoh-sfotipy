from rest_framework import serializers
from .models import Playlist

class PlaylistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Playlist
		depth = 5