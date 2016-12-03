"""ECrab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ECrab_Web import views

urlpatterns = [
	url(r'^$', views.landing),
    url(r'^login/$', views.login), 
	url(r'^login_redirect/$', views.login_redirect),
    url(r'^home/$', views.home),
    url(r'^perfil/$' ,views.perfil),
	url(r'^admin/', include(admin.site.urls)), #Check syntax
    url(r'^post/$', views.post)
#	url(r'^perfil/(?:<nombre_usuario>[a-z]*)$', views.perfil) #TODO: Implementar perfiles
    ]
