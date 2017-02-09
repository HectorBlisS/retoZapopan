import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action



def create_action(user, verb, target=None):
	#checamos cualquier acción similar en el ultimo minuto
	
	# if postreges in the filter: timestamp__gte=last_minute
	# now = timezone.now()
	# last_minute = now - datetime.timedelta(seconds=60)
	similar_actions = Action.objects.filter(user_id=user.id, verb=verb)
	if target:
		target_ct = ContentType.objects.get_for_model(target)
		similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)
	if not similar_actions:
		# no se ecnontraron acciones similares
		action = Action(user=user, verb=verb, target=target)
		action.save()
		return True
	return False