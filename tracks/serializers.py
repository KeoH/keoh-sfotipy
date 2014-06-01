from rest_framework import serializers
from .models import Track
from usersong_counts.models import CountSongUser

class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Track
		depth = 4

# class TopHitSerializer(serializers.HyperlinkedModelSerializer):

# 	total_playings = serializers.SerializerMethodField('get_played')

# 	def get_played(self, obj):
# 		return obj.get_listened()

# 	class Meta:
# 		model = Track
# 		fields = ('url', 'title', 'total_playings')
