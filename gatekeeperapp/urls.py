__author__ = 'rt'
from django.conf.urls import url, include

from gatekeeperapp import models, views
from .views import *
#from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

        url(r'^$', views.landing, name='landing'),
        url(r'^piechart/$', views.piechart, name='pie'),
        url(r'^search/$', views.search, name='search'),
        url(r'^tvehicles/$', views.tvehicles, name='tvehicles'),
        url(r'^twohours/$', views.twohours, name='twohours'),
        url(r'^report/$', views.report, name='report'),
        url(r'^gentryin/$', views.gentryin, name='gentryin'),
        url(r'^gentryout/$', views.gentryout, name='gentryout'),
        url(r'^search/(?P<slug>\S+)/$', views.search, name='search'),
#        url(r'^api/vehicle/$', views.VehicleList.as_view()),
		
       ]
