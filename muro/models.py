from django.db import models
from django.contrib.auth.models import User
from projects.models import Project



class Post(models.Model):
	body = models.TextField()
	user = models.ForeignKey(User, related_name='posts')
	date = models.DateTimeField(auto_now_add=True)
	project = models.ForeignKey(Project, blank=True, null=True)
