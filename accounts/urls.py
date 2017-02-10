from django.conf.urls import url
from django.contrib.auth.views import logout, login
from . import views


urlpatterns = [
    url(r'^signup/$', views.Registration.as_view(),name="signup"),
	url(r'^profile/$', views.Profiles.as_view(), name="profile"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),

	  # Listado de usuarios para seguirlos
  	url(r'^users/$',
    views.UserList.as_view(),
    name="user_list"),

	  # ajax para seguir o dejar de seguir
  	url(r'^users/follow/$',
    views.user_follow,
    name="user_follow"),

  # detalle de un usuario
  	url(r'^users/(?P<username>[-\w]+)/$',
    views.UserDetail.as_view(),
    name="user_detail"),
]