from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^(?P<id>[^/.]+)/$', views.get_user_details),
    url(r'^(?P<id>[^/.]+)/projects', views.get_user_projects),
]
