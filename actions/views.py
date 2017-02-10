from django.shortcuts import render, redirect
from django.contrib import messages
from muro.forms import PostForm
from django.views.generic import View
from actions.utils import create_action



class NewPost(View):
	def post(self, request):
		form = PostForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.user = request.user
			p.save()
			messages.success(request, 'Tu post se ha publicado')
			create_action(request.user, 'ha publicado un post',p)
			return redirect('dash:dash')
		messages.error(request, "Algo pasó no se puedo publicar tu post, intenta de nuevo")
		return redirect('dash:dash')
