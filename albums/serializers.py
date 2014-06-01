from .models import Album
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):

	image = serializers.SerializerMethodField('get_cover')

	def get_cover(self, obj):
		return obj.get_cover()

	class Meta:
		model = Album
		depth = 1
		fields = ('title', 'artist', 'image')