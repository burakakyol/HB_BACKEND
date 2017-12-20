from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('pk', 'title', 'description', 'is_active',
                  'is_completed', 'manager', 'process', 'progress', 'start_date')
