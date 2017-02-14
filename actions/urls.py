from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^new_post$',
		views.NewPost.as_view(),
		name="new_post"),

]