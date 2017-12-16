from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_process/', views.create_process),
    url(r'^(?P<id>[^/.]+)/$', views.get_process),
    url(r'^(?P<id>[^/.]+)/members/$', views.get_process_members),
    url(r'^(?P<id>[^/.]+)/members/add', views.add_process_member),

]
