from django.shortcuts import render

from django.contrib.auth.models import User
from process.models import Process, ProcessUser
from . import models
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from . import serializers


@api_view(['POST'])
def create_task(request):
    title = request.data.get('title')
    description = request.data.get('description')

    process_id = request.data.get('process_id')
    manager_id = request.data.get('manager_id')

    process = Process.objects.get(id=process_id)
    manager = ProcessUser.objects.get(id=manager_id)

    try:
        task = models.Task(
            title=title, description=description, process=process, manager=manager)
        task.save()
        return Response({'message': 'Görev başarıyla oluşturuldu', 'task_id': task.id,  'status': True})
    except:
        return Response({'message': 'Bir hata oluştu', 'status': False})
