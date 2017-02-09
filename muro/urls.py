from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^$',
		views.Muro.as_view(),
		name="muro"),
]