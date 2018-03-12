from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from smtplib import SMTP
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from nh5.serializers import EmployeeSerializer
from nh5.models import Employee
from django.core import serializers
import json

#from django.contrib.auth.models import User
#import datetime# Create your views here.





def appwebview(request):
    context_dict = {}
    return render(request, 'project/appwebview.html', context_dict)


def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    return render_to_response('nh5/index2.html', {}, context)
    


class EmployeeView(generics.ListCreateAPIView):
    """
    Returns a list of all authors.
    """
    model = Employee
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        queryset = Employee.objects.all()
        return queryset.order_by('-id')


def contact(request):
    context = RequestContext(request)
    #contacts = Employee.objects.all()
    #data = serializers.serialize("json", contacts)
    #return HttpResponse(json.dumps(data), content_type="application/json")
    return render_to_response('project/contacts.html', {}, context)

def contacts(request):
    context = RequestContext(request)
    contacts = Employee.objects.all()
    data = serializers.serialize("json", contacts)
    return HttpResponse(json.dumps(data), content_type="application/json")
    #return render_to_response('project/contacts.html', {}, context)
