from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_project/', views.create_project),
    url(r'^(?P<id>[^/.]+)/$', views.get_project),
    url(r'^(?P<id>[^/.]+)/members/add', views.add_member),
]
