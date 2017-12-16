from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class Process(models.Model):
    title = models.CharField(blank=False, null=False, max_length=170)
    description = models.TextField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project)
    is_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % (self.title)


ROLES_IN_PROCESS = (
    (0, 'Process Manager'),
    (1, 'Process Member'),


)


class ProcessUser(models.Model):
    user = models.ForeignKey(User)
    process = models.ForeignKey(Process)
    is_active = models.BooleanField(default=True)
    joining_date = models.DateField(auto_now=True)
    role = models.IntegerField(choices=ROLES_IN_PROCESS, default=1)

    def __str__(self):
        return '%s-%s-%s' % (self.user.username, self.process.title, self.role)
