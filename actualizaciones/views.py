from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import Update
from projects.models import Project
from django.core.urlresolvers import reverse_lazy

from django.contrib import messages

# crear actions
from actions.utils import create_action
# Enviar mails
from mailing.utils import Mailing



class NewUpdate(CreateView):
	model = Update
	template_name = 'actualizaciones/new.html'
	fields = ['title','body','img']
	project = None
	mailin = Mailing()
	def get_success_url(self):
		return reverse_lazy('actualizaciones:new', args=[self.project.id])

	def dispatch(self, request, pk):
		self.project = get_object_or_404(Project, id=pk)
		return super(NewUpdate, self).dispatch(request, pk)


	def get_form(self):
		form = super(NewUpdate, self).get_form()
		# the actual modification of the form
		form.instance.project = self.project
		return form

	def get_context_data(self, **kwargs):
		context = super(NewUpdate, self).get_context_data(**kwargs)
		context['project'] = self.project
		context['section'] = 'actualizaciones'
		return context

	def form_valid(self, form):
		messages.success(self.request, "Tu actualización se ha publicado con éxito")
		create_action(self.request.user, 'ha publicado una actualizacion de su proyecto',self.project)
		self.mailin.update(project=self.project)
			# print('se pudo')
		# except:
		# 	print('no se pudo')
		return super(NewUpdate, self).form_valid(form)  
