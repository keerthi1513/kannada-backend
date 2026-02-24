from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    age_group = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    native_region = models.CharField(max_length=100)
    schooling_region = models.CharField(max_length=100)
    writing_fluency = models.CharField(max_length=50)
    reading_fluency = models.CharField(max_length=50)
    speaking_fluency = models.CharField(max_length=50)
    hand = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class CharacterSample(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    character = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='characters/')
    timestamp = models.BigIntegerField()