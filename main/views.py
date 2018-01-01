from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from . import serializers

from project.models import Project, ProjectUser
from project.serializers import ProjectSerializer, ProjectUserSerializer

from task.models import Task, TaskUser
from task.serializers import TaskSerializer, TaskUserSerializer

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


''' curl --request POST --url http://localhost:8000/user/register/ --header 'content-type:application/json' --data '{"userna
me":"buraks9","password":"ps1oqmaq",}'
'''


@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    name = request.data.get("name")
    surname = request.data.get("surname")
    password = request.data.get("password")
    email = request.data.get("email")

    if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        User.objects.create_user(
            username=username, email=email, password=password, first_name=name, last_name=surname)
        return Response({"message": "Başarıyla kayıt oldunuz", "status": True})
    else:
        return Response({"error": "Kullanıcı ya da email adresiniz sistemde bulunmaktadır."})

# curl --request GET --url http://localhost:8000/user/3/ --header 'content-type:application/json'


@api_view(['GET'])
def get_user_details(request, id):

    try:
        user = User.objects.get(id=id)
        serializer = serializers.UserSerializer(user)

        return Response({"user": serializer.data})
    except User.DoesNotExist:
        return Response({"error": "User not found"})


@api_view(['POST'])
def search(request):
    query = request.data.get('query')
    try:
        q1 = User.objects.filter(username__startswith=query)
        serializer = serializers.UserSerializer(q1, many=True)
        return Response({'users': serializer.data, 'status': True})
    except:
        return Response({'error': 'Bir hata oluştu', 'status': False})


@api_view(['GET'])
def get_user_projects(request, id):

    try:
        user = User.objects.get(id=id)
        projects = ProjectUser.objects.filter(user=user)
        serializer = ProjectUserSerializer(projects, many=True)
        return Response({'projects': serializer.data})
    except:
        return Response({'message': 'Bir hata oluştu'})
