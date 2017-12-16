from django.shortcuts import render

from . import serializers
from django.contrib.auth.models import User
from . import models
from project.models import Project
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(['POST'])
def create_process(request):
    title = request.data.get('title')
    description = request.data.get('description')
    end_date = request.data.get('end_date')
    project_id = request.data.get('project_id')

    project = Project.objects.get(id=project_id)

    try:
        process = models.Process(
            title=title, description=description, end_date=end_date, project=project)
        process.save()
        return Response({'message': 'Süreç başarıyla oluşturuldu', 'status': True})
    except:
        return Response({'message': 'Bir hata oluştu', 'status': False})


@api_view(['GET'])
def get_process(request, id):
    try:
        process = models.Process.objects.get(id=id)
        serializer = serializers.ProcessSerializer(process)

        return Response({"process": serializer.data})
    except models.Process.DoesNotExist:
        return Response({"error": "Süreç bulunamadı"})


@api_view(['GET'])
def get_process_members(request, id):
    try:
        process = models.Process.objects.get(id=id)
        members = models.ProcessUser.objects.filter(process=process)

        process_serializer = serializers.ProcessSerializer(process)
        members_serializer = serializers.ProcessUserSerializer(
            members, many=True)

        return Response({'members': members_serializer.data, 'process': process_serializer.data['title']})
    except models.Process.DoesNotExist:
        return Response({"error": "Süreç bulunamadı"})


@api_view(['POST'])
def complete_process(request, id):
    try:
        process = models.Process.objects.get(id=id)
        process.is_completed = True
        process.save()

        return Response({'message': 'Süreç başarıyla tamamlandı', 'status': True})
    except models.Process.DoesNotExist:
        return Response({"error": "Süreç bulunamadı"})


@api_view(['POST'])
def close_process(request, id):
    try:
        process = models.Process.objects.get(id=id)
        process.is_active = False
        process.save()

        return Response({'message': 'Süreç kapatıldı', 'status': True})
    except models.Process.DoesNotExist:
        return Response({"error": "Süreç bulunamadı"})


@api_view(['POST'])
def add_process_member(request, id):
    user_id = request.data.get('user_id')
    try:
        process = models.Process.objects.get(id=id)

        user = User.objects.get(id=user_id)

        process_user = models.ProcessUser(
            user=user, process=process, role=0)
        process_user.save()
        return Response({'message': 'Kullanıcı başarıyla sürece eklendi', 'status': True})
    except models.Process.DoesNotExist:
        return Response({'message': 'Bir hata oluştu', 'status': False})
