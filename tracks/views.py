from rest_framework import viewsets
from .serializers import TrackSerializer#, TopHitSerializer
from .models import Track
#from usersong_counts.models import CountSongUser

class TrackViewSet(viewsets.ModelViewSet):
	model = Track
	serializer_class = TrackSerializer

# class TophitsViewSet(viewsets.ModelViewSet):
# 	model = Track
# 	serializer_class = TopHitSerializer