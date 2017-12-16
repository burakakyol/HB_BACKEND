from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_process/', views.create_process),

]
