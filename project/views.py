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
