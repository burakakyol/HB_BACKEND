from . import models
from rest_framework import serializers


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Process
        fields = ('pk', 'title', 'description', 'start_date',
                  'end_date', 'project', 'is_completed', 'is_active')
