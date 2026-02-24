from rest_framework import viewsets
from .models import UserProfile, CharacterSample
from .serializers import UserSerializer, CharacterSampleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class CharacterSampleViewSet(viewsets.ModelViewSet):
    queryset = CharacterSample.objects.all()
    serializer_class = CharacterSampleSerializer