__author__ = 'rt'
from django.conf.urls import patterns, url
from nh5 import views, models
from registration.backends.default.views import RegistrationView
from nh5.forms import CustomUserCreationForm


urlpatterns = patterns('',
        url(r'^$', views.index, name ='index'),
	       # url(r'^index/', views.index, name ='index'),
       # url(r'^clients/', views.clients, name ='clients'),
	#url(r'^services/', views.services, name ='services'),
        #url(r'^contact/$', views.contact, name = 'contact'),
      #  url(r'^sendmsg/$', views.sendmsg, name='sendmsgcli'),
       # url(r'^thanks/$', views.thanks, name='thanks'),
        #url(r'^about/$', views.about, name='about'),
	#url(r'^news/$', views.news, name='news'),
       )
