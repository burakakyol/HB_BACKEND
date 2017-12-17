from django.db import models
from django.contrib.auth.models import User
from process.models import Process, ProcessUser


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    process = models.ForeignKey(Process)
    manager = models.ForeignKey(ProcessUser)
    is_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    progress = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return "%s" % (self.title)


class TaskUser(models.Model):
    task = models.ForeignKey(Task)
    member = models.ForeignKey(ProcessUser)
