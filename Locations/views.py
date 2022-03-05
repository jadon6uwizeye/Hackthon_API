from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model
from .serializers import *
User = get_user_model()


class UsersInLocalty(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, format=None):
        users = User.objects.filter(address__district= request.user.address__district)
        
        return Response(AccountSerializer(users, many=True).data)
