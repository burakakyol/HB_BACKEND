from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from main.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('pk', 'title', 'description', 'start_date', 'end_date',)


class ProjectUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = models.ProjectUser
        fields = ('pk', 'user', 'project', 'joining_date', 'role', 'is_active')
