
from rest_framework import serializers
from . import models

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta: User
        model = models.CustomUser
        fields = ('email', 'username', )