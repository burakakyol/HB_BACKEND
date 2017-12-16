from django.shortcuts import render

from django.contrib.auth.models import User
from . import models
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
# Create your views here.
