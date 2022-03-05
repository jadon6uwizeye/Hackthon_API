from django.shortcuts import render
from rest_framework import generics

# Create your views here.

from . import models
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
