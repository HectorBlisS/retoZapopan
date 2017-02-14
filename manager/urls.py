from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^(?P<cat>[-\w]+)/$',views.ManageView.as_view(), name="cat" ), 	
	url(r'^status/(?P<status>[-\w]+)/$', views.ManageView.as_view(), name="stat"),
	url(r'^detail/(?P<pk>\d+)/$', views.ManageDetail.as_view(), name='detail'),
	url(r'^$',views.ManageView.as_view(), name="manage" ),
	
]