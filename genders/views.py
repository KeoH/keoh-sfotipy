from rest_framework import viewsets
from .models import Gender
from .serializers import GenderSerializer

class GenderViewSet(viewsets.ModelViewSet):
	model = Gender
	serializer_class = GenderSerializer
