from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('pk', 'title', 'description', 'start_date', 'end_date',)
