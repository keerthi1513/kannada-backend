from rest_framework import serializers
from .models import UserProfile, CharacterSample

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CharacterSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSample
        fields = '__all__'