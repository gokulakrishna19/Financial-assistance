"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from signup.views import *
from machine.views import detail1

#from mysite.core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', detail1),
    url(r'^machine/', include('machine.urls')),
    url(r'^fixeddeposit/', include('fixeddeposit.urls')),
    url(r'^realestate/', include('realestate.urls')),
    url(r'^stockmarket/', include('stockmarket.urls')),
    url(r'^mutualfund/', include('mutualfund.urls')),
    url(r'^insurance/', include('insurance.urls')),
    url(r'^signup/', include('signup.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^home/$', home),
    url(r'^logout/$', logout_page),
    url(r'^register/success/$', register_success),
    
    #url(r'^signup/', core_views.signup, include('signup.urls')),


]
