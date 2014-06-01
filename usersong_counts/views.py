from rest_framework import viewsets
from .models import CountSongUser
from .serializers import CountSongUserSerializer

class CountSongUserViewSet(viewsets.ModelViewSet):
	model = CountSongUser
	serializer_class = CountSongUserSerializer