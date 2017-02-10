from django.conf.urls import url
from . import views

urlpatterns=[
	#url(r'^(?P<cat>[-\w]+)/$',views.ManageView.as_view(), name="cat" ), 
	url(r'^$',views.ManageView.as_view(), name="manage" ),
	
	url(r'^(?P<pk>\d+)/$', views.ManageDetail.as_view(), name='detail'),
]