from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View
from .models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

# follow users
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Mixins para login y response
from braces.views import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.models import User

# from common.decorators import ajax_required
from .models import Contact

# Activity stream actions
from actions.utils import create_action
# from actions.models import Action


# <- Listado de usuarios para seguirlos
class UserList(LoginRequiredMixin, TemplateResponseMixin, View):
	template_name = "accounts/user/list.html"
	def get(self, request):
		users = User.objects.filter(is_active=True)
		return self.render_to_response({'section':'people','users':users})

class UserDetail(LoginRequiredMixin, TemplateResponseMixin, View):
	template_name="accounts/user/detail.html"
	def get(self, request, username):
		user = get_object_or_404(User, username=username, is_active=True)
		return self.render_to_response({'section':'people','user':user})
# Listado de usuarios para seguirlos ->

# Seguir y dejar de seguir usuarios
@require_POST
@login_required
def user_follow(request):
	if request.is_ajax():
		user_id = request.POST.get('id')
		action = request.POST.get('action')
		if user_id and action:
			try:
				user = User.objects.get(id=user_id)
				if action == 'follow':
					Contact.objects.get_or_create(
						user_from=request.user,
						user_to=user)
					create_action(request.user, 'está siguiendo a', user)
				else:
					Contact.objects.filter(user_from=request.user,
						user_to=user).delete()
				return JsonResponse({'status':'ok'})
			except User.DoesNotExist:
				return JsonResponse({'status':'ko'})
	return JsonResponse({'status':'ko'})


class Profiles(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="accounts/perfil.html"
		userform = UserEditForm(instance=request.user)
		profileform = ProfileEditForm(instance=request.user.profile)
		context = {
		'userform':userform,
		'profileform':profileform,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name="accounts/perfil.html"
		userform = UserEditForm(instance=request.user,data=request.POST)
		profileform = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
		if userform.is_valid() and profileform.is_valid():
			userform.save()
			profileform.save()
			return redirect('accounts:profile')
		else:
			context={
			'userform':userform,
			'profileform':profileform,
			}
			return render(request,template_name,context)
		
class Registration(View):
	def get(self, request):
		template_name = "accounts/registration.html"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "accounts/registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			# perfil = Profile(instance=new_user)
			new_user.save()
			Profile.objects.create(user=new_user)
			#perfil = Profile()
			#perfil.user = new_user
			#perfil.save()
			# perfil = Profile.objects.create(user=new_user)

			new_user = authenticate(username=new_user_form.cleaned_data['username'],
                                    password=new_user_form.cleaned_data['password'],
                                    )
			login(request, new_user)

			return redirect('dash:dash')
		else:
			context = {
			'form':new_user_form
			}
			return render(request,template_name,context)





