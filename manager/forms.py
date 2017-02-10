from django import forms
from projects.models import Project

class ManagerForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['status', 'goal']