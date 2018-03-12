__author__ = 'rt'
from django.conf.urls import patterns, url
from nh5 import views
from nh5.views import EmployeeView
from rest_framework.urlpatterns import format_suffix_patterns
from nh5.forms import CustomUserCreationForm


urlpatterns = patterns('',
        #url(r'^$', views.index, name ='index'),
	url(r'^contacts/$', EmployeeView.as_view(), name='employee-list'),
	url(r'^contact/$', views.contact, name='xemployee-list'),
       # url(r'^clients/', views.clients, name ='clients'),
	#url(r'^services/', views.services, name ='services'),
        #url(r'^contact/$', views.contact, name = 'contact'),
      #  url(r'^sendmsg/$', views.sendmsg, name='sendmsgcli'),
       # url(r'^thanks/$', views.thanks, name='thanks'),
        #url(r'^about/$', views.about, name='about'),
	url(r'^appwebview/$', views.appwebview, name='appwebview'),
       )


urlpatterns = format_suffix_patterns(urlpatterns)
