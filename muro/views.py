from django.shortcuts import render
from django.views.generic import View
from actions.models import Action

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



# Create your views here.
class Muro(View):
	@method_decorator(login_required)
	def get(self, request):
		#mostramos todas las acciones por default
		actions = Action.objects.exclude(user=request.user)
		following_ids = request.user.following.values_list('id',flat=True)
		if following_ids:
			# si el usuario está siguiendo a otros, filtramos las acciones
			# actions = actions.filter(user_id__in=following_ids)
			# optimizando la peticion:
			actions = actions.filter(user_id__in=following_ids).select_related('user','user__profile').prefetch_related('target')
		actions = actions[:10]
		template_name = 'muro/inicio.html'
		context = {
			'actions':actions,
			#'form_user':form_user
		}
		return render(request, template_name, context)