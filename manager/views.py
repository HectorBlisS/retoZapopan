from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import UpdateView
from projects.models import Project
from taggit.models import Tag
from django.core.urlresolvers import reverse_lazy
from .forms import ManagerForm
from django.contrib import messages

# Create your views here.
class ManageView(View):
	
	def get(self, request, cat=None, status=None):
		template_name = 'manager/list.html'
		if status:
			projects = Project.objects.all().filter(status=status)	
		elif cat:
			projects = Project.objects.all().filter(tags__name__in=[cat])
		else:
			projects = Project.objects.all()
		

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

	def post(self, request, pk):
		template_name = "manager/detail.html"
		p = get_object_or_404(Project, id=pk)
		data = request.POST
		form = ManagerForm(data, instance=p)
		print(form)
		# print(form)

		if form.is_valid():
			form.save()
			print('PASO Y GUARDO')
			messages.success(request, "Proyecto guardado con éxito")
		else:
			print('No es Valido')
			messages.error(request, "El proyecto no se guardó")

		context = {
			'project':p
		}
		return render(request, template_name,context)




