__author__ = 'rt'
from django.conf.urls import patterns, url
from nh5 import views, models
from registration.backends.default.views import RegistrationView
from nh5.forms import CustomUserCreationForm


urlpatterns = patterns('',
        url(r'^$', views.index, name ='index'),
	      
       )
