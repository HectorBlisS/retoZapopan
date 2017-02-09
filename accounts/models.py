from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    img = models.ImageField(upload_to='profile_img', blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
    	return 'Perfil del usuario {}'.format(self.user.username)


class Contact(models.Model):
	user_from = models.ForeignKey(User, related_name='rel_from_set')
	user_to = models.ForeignKey(User, related_name='rel_to_set')
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} follows {}'.format(self.user_from, self.user_to)



# Modificamos al modelo User de forma dinamica
User.add_to_class('following',
	models.ManyToManyField('self', 
		through=Contact,
		related_name='followers',
		symmetrical=False))