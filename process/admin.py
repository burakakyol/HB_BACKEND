from django.contrib import admin
from . import models

admin.site.register(models.Process)
admin.site.register(models.ProcessUser)

# Register your models here.
