from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accountsURLs
from social.apps.django_app import urls as socialURLs
# from social_django import urls as socialURLs
from main import urls as mainUrls
from inputs import urls as inputsURLs
from dashboard import urls as dashboardURLs
from projects import urls as projectsURLs
from cart import urls as cartURLs
from manager import urls as managerUrls

from django.views.static import serve
from django.conf import settings

# muro
from muro import urls as muroUrls
from actions import urls as actionsUrls
# Actualizaciones
from actualizaciones import urls as acUrls


urlpatterns = [

    #main
    url(r'^', include(mainUrls)),

    url(r'^inputs/',
        include(inputsURLs)),

    url(r'^dashboard/',
        include(dashboardURLs, namespace="dash")),

    url(r'^projects/',
        include(projectsURLs, namespace="projects")),

    url(r'^accounts/',
        include(accountsURLs)),

    url(r'^cart/',
        include(cartURLs, namespace="cart")),


    url(r'^manager/', 
        include(managerUrls, namespace="manager")),

    url(r'^muro/',
        include(muroUrls, namespace="muro")),

    url(r'^actions/',
        include(actionsUrls, namespace="actions")),

    url(r'^actualizaciones/',
        include(acUrls, namespace="actualizaciones")),

    #Django Admin
    url(r'^admin/', admin.site.urls),

    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),

    # Social Auth
    url('social-auth/',
        include(socialURLs,
            namespace="social")),

]
