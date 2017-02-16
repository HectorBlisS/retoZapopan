from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import Update
from projects.models import Project
from django.core.urlresolvers import reverse_lazy





class NewUpdate(CreateView):
	model = Update
	template_name = 'actualizaciones/new.html'
	fields = ['title','body','img']
	project = None

	def get_success_url(self):
		return reverse_lazy('dash:detail', args=[self.project.id])

	def dispatch(self, request, pk):
		self.project = get_object_or_404(Project, id=pk)
		return super(NewUpdate, self).dispatch(request, pk)


	def get_form(self):
		form = super(NewUpdate, self).get_form()
		# the actual modification of the form
		form.instance.project = self.project
		return form
