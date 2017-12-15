from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from core.models import Favorite
from core.serializers import ProjectSerializer, UserSerializer

class ProjectList(generics.ListCreateAPIView):
    """
    List all favorites
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

# Create your views here.
