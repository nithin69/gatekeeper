__author__ = 'rt'
from django.conf.urls import url, include

from gatekeeperapp import models, views
from .views import *
#from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

        url(r'^$', views.landing, name='landing'),
        url(r'^piechart/$', views.piechart, name='pie'),
        url(r'^piechartpage/$', views.piechartpage, name='piechart'),
        url(r'^search/$', views.search, name='search'),
        url(r'^tvehicles/$', views.tvehicles, name='tvehicles'),
        url(r'^twohours/$', views.twohours, name='twohours'),
        url(r'^report/$', views.report, name='report'),
        url(r'^gentryin/$', views.gentryin, name='gentryin'),
        url(r'^gentryout/$', views.gentryout, name='gentryout'),
        #url(r'^search/(?P<slug>\S+)/$', views.search, name='search'),
        url(r'^managersearch/$', views.managersearch, name='managersearch'),
        url(r'^guardsearch/$', views.guardsearch, name='guardsearch'),
        url(r'^autocomplete/get/$',AutoCompleteView.as_view(), name='autocomplete'),
        url(r'^autocompleteout/get/$',AutoCompleteOut.as_view(), name='autocompletecon'),
        url(r'^autocomplete/getcharges/',AutoCompleteCharges.as_view(), name='autocompletecharges'),

#        url(r'^api/vehicle/$', views.VehicleList.as_view()),
		
       ]
