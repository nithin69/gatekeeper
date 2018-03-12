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

#from django.contrib.auth.models import User
#import datetime# Create your views here.



def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    return render_to_response('nh5/index2.html', {}, context)
    
