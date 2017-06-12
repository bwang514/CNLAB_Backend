"""
mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from trips.views import home
from trips.handle import *

urlpatterns = [
	url(r'^isLoginSuccess', isloginsuccess),
	url(r'^setUserAccount', setuseraccount),
	url(r'^changePassword', changepassword),
	url(r'^getUserPhoto', getuserphoto),
	url(r'^getUserVoice', getuservoice),
	url(r'^setUserPhoto', setuserphoto),
	url(r'^setUserVoice', setuservoice),
	url(r'^image', image),
	url(r'^audio', audio),
	url(r'^username', username),
	# url(r'^isLoginSuccess', isLoginSuccess),
	# url(r'^isLoginSuccess', isLoginSuccess),
	# url(r'^isLoginSuccess', isLoginSuccess),
	# url(r'^isLoginSuccess', isLoginSuccess),
	url(r'^$', home, name="home"),
    url(r'^admin/', include(admin.site.urls)),
]
