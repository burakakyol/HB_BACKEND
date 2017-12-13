from django.contrib import admin
from .models import Project

class Project_Page(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'title', 'desc')
    search_fields = ('start_date', 'end_date', 'title', 'desc')
 
admin.site.register(Project,Project_Page)
    
