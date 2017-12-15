from django.shortcuts import render

from django.contrib.auth.models import User
from . import models
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from . import serializers
# Create your views here.


@api_view(['POST'])
def create_project(request):
    title = request.data.get('title')
    description = request.data.get('description')
    end_date = request.data.get('end_date')

    try:
        project = models.Project(
            title=title, description=description, end_date=end_date)
        project.save()
        return Response({'message': 'Proje başarıyla oluşturuldu', 'status': True})
    except:
        return Response({'message': 'Bir hata oluştu', 'status': False})

# project/$(id)/members/add


'''
curl --request POST --url http://127.0.0.1:8000/project/1/members/add/ --header 'content-type:application/json' --dat
a '{"user_id":1}'
'''


@api_view(['POST'])
def add_member(request, id):
    user_id = request.data.get('user_id')
    try:
        project = models.Project.objects.get(id=id)

        user = User.objects.get(id=user_id)

        project_user = models.ProjectUser(
            user=user, project=project, role=0)
        project_user.save()
        return Response({'message': 'Kullanıcı başarıyla projeye eklendi', 'status': True})
    except models.Project.DoesNotExist:
        return Response({'message': 'Bir hata oluştu', 'status': False})


@api_view(['GET'])
def get_project(request, id):
    try:
        project = models.Project.objects.get(id=id)
        serializer = serializers.ProjectSerializer(project)

        return Response({"project": serializer.data})
    except models.Project.DoesNotExist:
        return Response({"error": "Proje bulunamadı"})


@api_view(['PUT'])
def update_project(request, id):
    title = request.data.get('title')
    description = request.data.get('description')
    end_date = request.data.get('end_date')

    try:
        project = models.Project(
            id=id, title=title, description=description, end_date=end_date)
        project.save()
        serializer = serializers.ProjectSerializer(project)
        return Response({"project": serializer.data})
    except models.Project.DoesNotExist:
        return Response({"error": "Proje bulunamadı"})
