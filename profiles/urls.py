from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
#from blog.models import Post

urlpatterns = [ 
                url(r'^$', views.index, name='index' ),
            ]