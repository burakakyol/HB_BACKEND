from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_task/', views.create_task),


]
