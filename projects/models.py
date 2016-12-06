from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    user = models.ForeignKey(User, related_name="projects")
    goal = models.DecimalField(max_digits=7,decimal_places=2,default=1)


class Comments(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)