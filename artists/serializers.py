from .models import Artist, Country
from rest_framework import serializers
from core.settings import MY_URL, DEBUG


class CountrySerializer(serializers.ModelSerializer):

	continent_verbose = serializers.SerializerMethodField('get_continent')

	def get_continent(self, obj):
		return obj.get_continent()

	class Meta:
		model = Country
		fields = ('name', 'continent', 'continent_verbose')

class ArtistSerializer(serializers.ModelSerializer):
	
	fullname = serializers.SerializerMethodField('get_fullname')
	prof_img = serializers.SerializerMethodField('get_profile_image')

	def get_fullname(self, obj):
		return obj.fullname()

	def get_profile_image(self, obj):

		return obj.get_profile_image()

	class Meta:
		model = Artist
		depth = 1
		fields = ('first_name','last_name','fullname', 'biography', 'country','prof_img', 'is_group')