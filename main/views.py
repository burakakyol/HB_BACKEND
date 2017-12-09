from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from . import serializers

''' curl --request POST --url http://localhost:8000/user/login/ --header 'content-type:application/json' --data '{"userna
me":"buraks9","password":"ps1oqmaq"}'
'''

# asdasd


@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        serializer = serializers.UserSerializer(user)
        return Response({"token": token.key, "user": serializer.data})
    return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        User.objects.create_user(
            username=username, email=email, password=password)
        return Response({"status": "You have been succesfully registered"})
    else:
        return Response({"error": "Username or email already exists"})

# curl --request GET --url http://localhost:8000/user/3/ --header 'content-type:application/json'


@api_view(['GET'])
def get_user_details(request, id):

    try:
        user = User.objects.get(id=id)
        serializer = serializers.UserSerializer(user)

        return Response({"user": serializer.data})
    except User.DoesNotExist:
        return Response({"error": "User not found"})
