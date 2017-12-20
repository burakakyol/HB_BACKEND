from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_task/', views.create_task),
    url(r'^(?P<id>[^/.]+)/$', views.get_task),
    url(r'^(?P<id>[^/.]+)/members/add', views.add_task_member),
    url(r'^(?P<id>[^/.]+)/update', views.update_task),


]
