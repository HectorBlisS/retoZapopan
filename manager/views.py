from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from projects.models import Project
from taggit.models import Tag

# Create your views here.
class ManageView(View):
	
	def get(self, request, cat=None):
		template_name = 'manager/list.html'
		projects = Project.objects.all()
		
		
		#if cat:
		#	tag = get_object_or_404(Tag, slug=self.kwargs['cat'])
		#	projects = Project.objects.all().filter(tags__in=[tag])
		#else:
		#	projects = Project.objects.all()
		#	tag = Tag.objects.all()

		context={
		'projects': projects,
		}

		return render(request, template_name, context)


class ManageDetail(View):

	def get(self, request, pk):
		template_name = "manager/detail.html"
		project = get_object_or_404(Project, id=pk)
		context = {
		'project': project
		}

		return render(request, template_name, context)



