from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from projects.models import Project
from .forms import BasicsForm

from django.contrib import messages

class Dash(View):
	def get(self, request):
		template_name = "dashboard/projects_list.html"
		p = request.user.projects.all()
		context = {
			'projects':p
		}
		return render(request, template_name,context)

class Detail(View):
	def get(self, request, pk):
		template_name = "dashboard/dash.html"
		p = get_object_or_404(Project, id=pk)
		context = {
			'project':p,
			'section':'dash'
		}
		return render(request, template_name,context)

class Basics(View):
	def get(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		form = BasicsForm()
		context = {
			'project':p,
			'section':'basics',
			'form':form
		}
		return render(request, template_name,context)

	def post(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		data = request.POST.dict()
		form = BasicsForm(data,request.FILES,instance=p)
		# print(form)

		if form.is_valid():
			form.save()
			print('PASO Y GUARDO')
			messages.success(request, "Proyecto guardado con éxito")
		else:
			print('No es Valido')
			messages.error(request, "El proyecto no se guardó")

		context = {
			'project':p,
			'section':'basics',
		}
		return render(request, template_name,context)


class History(View):
	def get(self, request, pk):
		template_name = "dashboard/history.html"
		p = get_object_or_404(Project, id=pk)
		context = {
			'project':p,
			'section':'history'
		}
		return render(request, template_name,context)

	def post(self, request, pk):
		template_name = "dashboard/history.html"
		p = get_object_or_404(Project, id=pk)
		data = request.POST.dict()
		form = BasicsForm(data,request.FILES,instance=p)
		# print(form)

		if form.is_valid():
			form.save()
			print('PASO Y GUARDO')
			messages.success(request, "Proyecto guardado con éxito")
		else:
			print('No es Valido')
			messages.error(request, "El proyecto no se guardó")

		context = {
			'project':p,
			'section':'history',
		}
		return render(request, template_name,context)



class Team(View):
	def get(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		context = {
			'project':p,
			'section':'team'
		}
		return render(request, template_name,context)

class Extra(View):
	def get(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		context = {
			'project':p,
			'section':'extra'
		}
		return render(request, template_name,context)

