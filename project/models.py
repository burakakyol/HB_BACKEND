from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(blank=False, null=False, max_length=170)
    description = models.TextField()
    start_date = models.DateField(auto_now=True)
    end_Date = models.DateField()

    def __str__(self):
        return '%s' % (self.title)


ROLES_IN_PROJECT = (
    (0, 'Project Owner'),
    (1, 'Project Member'),
    (2, 'Project Manager'),
    (3, 'Process Manager'),

)


class ProjectUser(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    is_active = models.BooleanField(default=True)
    joining_date = models.DateField(auto_now=True)
    role = models.IntegerField(choices=ROLES_IN_PROJECT, default=1)

    def __str__(self):
        return '%s-%s-%s' % (self.user.username, self.project.title, self.role)
