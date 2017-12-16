from django.shortcuts import render

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
