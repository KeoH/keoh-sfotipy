from .models import Gender
from rest_framework import serializers

class GenderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Gender