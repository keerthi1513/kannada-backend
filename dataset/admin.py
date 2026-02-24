from django.contrib import admin

from kannada_backend.settings import MEDIA_URL, MEDIA_ROOT
from .models import UserProfile, CharacterSample

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CharacterSample)