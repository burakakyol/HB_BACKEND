from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from process.serializers import ProcessUserSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('pk', 'title', 'description', 'is_active',
                  'is_completed', 'manager', 'process', 'progress', 'start_date')


class TaskUserSerializer(serializers.ModelSerializer):
    member = ProcessUserSerializer(many=False, read_only=True)
    task = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = models.TaskUser
        fields = ('pk', 'member', 'task')
