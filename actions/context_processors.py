from .models import Action

def my_actions(request):
	if not request.user.is_anonymous():
		return {
			'my_actions':Action.objects.exclude(user=request.user).filter(target_id=request.user.id)
		}
	
	return []