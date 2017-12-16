from . import models
from rest_framework import serializers
from main.serializers import UserSerializer


class ProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Process
        fields = ('pk', 'title', 'description', 'start_date',
                  'end_date', 'project', 'is_completed', 'is_active')


class ProcessUserSerializer(serializers.ModelSerializer):
    # bütün nesne geliyo user = UserSerializer(many=False, read_only=True)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.ProcessUser
        fields = ('pk', 'user', 'process', 'is_active', 'role')
