from django.contrib import admin
from . import models

admin.site.register(models.Project)
admin.site.register(models.ProjectUser)
# Register your models here.
