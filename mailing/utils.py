from django.template.loader import get_template
from django.core.mail import EmailMessage
# from projects.models import Project



class Mailing(object):
	def __init__(self):
		"""
		inicializamos
		"""
		# self.user = request.user
		self.to = []
		self.from_email = 'contacto@fixter.org'
		self.subject = "Reto Zapopan"
		self.ctx = None

	def update(self, project, subject=None):
		print('entre')
		self.get_followers(project)
		self.ctx = {'project':project}
		if subject:
			self.subject = subject
		self.send()

	def get_followers(self, project):
		user = project.user
		fs = user.followers.all()
		print(fs)
		lista = []
		for f in fs:
			lista.append(f.email)
		self.to = lista
		return True

	def send(self):
		message=get_template("mailing/update.html").render(self.ctx)
		msg=EmailMessage(self.subject,message,bcc=self.to,from_email=self.from_email)
		msg.content_subtype='html'
		return msg.send() 





