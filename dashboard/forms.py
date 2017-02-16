from django import forms
from projects.models import Project, Reward
from accounts.models import Profile
from projects.models import Project, Acciones


class ImgForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img', 'tel']


class BasicsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'goal', 'tags']


class HistoryForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['desc', 'video', 'img']


class NewRewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['title', 'price', 'desc', 'quantity', 'deliver_date']


class NewAccionesForm(forms.ModelForm):
    class Meta:
        model = Acciones
        fields = ['title', 'price', 'desc', 'quantity', 'deliver_date']
