from django.db import models

from model_utils.models import TimeStampedModel
# Create your models here.
class Project(TimeStampedModel):
    start_date = models.DateTimeField(default = timezone.now)
    end_date = models.DateTimeField()
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()
  
    def __str__(self):
        return ('{}'.format(self.title))
    
    
   
    
    
    
    
