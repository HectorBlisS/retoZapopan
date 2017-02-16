from django.db import models
from projects.models import Project


class Update(models.Model):
	project = models.ForeignKey(Project, related_name='updates')
	title = models.CharField(max_length=140)
	body = models.TextField()
	img = models.ImageField(upload_to='updates/images', blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Update for {}".format(self.project)

	class Meta:
		ordering = ['-created']
