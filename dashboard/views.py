from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from projects.models import Project, Reward
from accounts.models import Profile
from .forms import BasicsForm, HistoryForm, ImgForm, NewRewardForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from taggit.models import Tag

from actions.models import Action
from muro.forms import PostForm



class Dash(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "dashboard/perfil.html"
		projects = request.user.projects.all()
		# actions = Action.objects.exclude(user=request.user)exclude(user=request.user)
		actions = Action.objects.all()
		following_ids = request.user.following.values_list('id',flat=True)
		if following_ids:
			# si el usuario está siguiendo a otros, filtramos las acciones
			# actions = actions.filter(user_id__in=following_ids)
			# optimizando la peticion:
			actions = actions.filter(user_id__in=following_ids).select_related('user','user__profile').prefetch_related('target')
		actions = actions[:10]
		
		form = PostForm()

		context = {
			'projects':projects,
			'actions':actions,
			'form':form
		}
		return render(request, template_name, context)

	def post(self, request):
		try:
			profile = request.user.profile
		except:
			profile = Profile()
			profile.user = request.user
			profile.save()

		form = ImgForm(instance=request.user.profile,data=request.POST, files=request.FILES)
		print(form)
		print(request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Tu Perfil se actualizó con exito")
		else:
			messages.error(request, "Algo malo pasó, U_U intenta de nuevo")
		return redirect('dash:dash')

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
		cats = Tag.objects.all()
		context = {
			'project':p,
			'section':'basics',
			'form':form,
			'cats':cats
		}
		return render(request, template_name,context)

	def post(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		if p.publish:
			messages.error(request, "Tu proyecto ya se publicó, no puedes modificarlo")
			return redirect('dash:basics',pk=pk)
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
			'cats':Tag.objects.all()
			
		}
		return render(request, template_name,context)

import markdown2

class History(View):
	def get(self, request, pk):
		template_name = "dashboard/history.html"
		p = get_object_or_404(Project, id=pk)
		try:
			p.desc = markdown2.markdown(p.desc)
		except:
			pass
		context = {
			'project':p,
			'section':'history'
		}
		return render(request, template_name,context)

	def post(self, request, pk):
		template_name = "dashboard/history.html"
		p = get_object_or_404(Project, id=pk)
		data = request.POST.dict()
		form = HistoryForm(data, files=request.FILES,instance=p)
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
			'project':p,
			'section':'history',
		}
		return render(request, template_name,context)


class Rewards(View):
	def get(self, request, pk):
		template_name = "dashboard/rewards.html"
		p = get_object_or_404(Project, id=pk)
		rewards = p.rewards.all()
		context = {
			'project':p,
			'section':'recompensas',
			'rewards':rewards
		}
		return render(request, template_name, context)

	def post(self, request, pk):

		if request.POST.get('borrar'):
			r = get_object_or_404(Reward, id=request.POST.get('borrar'))
			r.delete()
			messages.success(request, "Haz borrado una recompensa")
			return redirect('dash:rewards',pk=pk)

		p = get_object_or_404(Project, id=pk)

		form = NewRewardForm(data=request.POST)
		if request.POST.get('pk'):
			r = get_object_or_404(Reward,id=request.POST.get('pk'))
			form = NewRewardForm(data=request.POST, instance=r)
		
		if form.is_valid():
			r = form.save(commit=False)
			r.project = p
			r.save()
			messages.success(request, "Tu recompensa se ha guardado con éxito")
			
		else:
			messages.error(request, "Algo malo pasó, U_U vuelve a intentarlo")
		return redirect('dash:rewards',pk=pk)


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




# Panels del lado del que apoya incluyendo chat

class Support(View):
	def get(self, request):
		template_name = "dashboard/founder.html"
		p = request.user.funds.all()
		context = {
			'projects':p
		}
		return render(request, template_name, context)

class Chating(View):
	def get(self, request, pk=None):
		template_name = "dashboard/mensajeria.html"
		# project = get_object_or_404(Project,id=pk)
		p = request.user.funds.all()
		print(request.user.cchats.all())
		# chat = request.user.cchats.all().get(project=project)
		
		context = {
			'projects':p,
			# 'chat':chat
		}
		return render(request, template_name, context)

