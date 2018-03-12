from django.contrib.auth.decorators import login_required
#from gateentry.forms import EntryForm
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from gateuser.models import Employee
import random
import datetime
import time
from datetime import datetime, timedelta, time
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from django.core import serializers
#from rest_framework import generics



#from dal import autocomplete

# Create your views here.


#admin/gatekeeperapp/vehicle/add/
@login_required  
def tvehicles(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    vehicle = Vehicle.objects.filter(time_of_entry__range=[today_start, today_end])
    context_dict = {'entries' : vehicle,}
    return render(request, 'gatekeeper/tvehicles.html', context_dict)


@login_required  
def twohours(request):
    import datetime as x
    twohours = x.datetime.now() - timedelta(hours=2)
    print twohours
    vehicle = Vehicle.objects.filter(time_of_entry__gte=twohours)
    context_dict = {'entries' : vehicle,}
    return render(request, 'gatekeeper/twohours.html', context_dict)



@login_required  
def landing(request):
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user = user)
    designation = employee.designation
    context_dict = {}
    if designation == 'guard':
        return render(request, 'gatekeeper/landing.html', context_dict)
    else:
        return render(request, 'gatekeeper/error.html', context_dict)

@login_required  
def report(request):
    
    context_dict = {}
    #return render(request, 'gatekeeper/report.html', context_dict)
    return render(request, 'gatekeeper/supervisor_report.html', context_dict)



@login_required
def search(request, slug, *args, **kwargs):
    if 'from_date' in request.GET:
        from_date = request.GET['from_date']
        print "from date ", from_date
    if 'to_date' in request.GET:
        to_date = request.GET['to_date']    
    print "to date", to_date
    vehicle = Vehicle.objects.filter(time_of_entry__range=[from_date, to_date])
    print vehicle
    context_dict = {'entries' : vehicle}
    print "abbhh"
    return render(request, 'gatekeeper/supervisor_search_report.html', context_dict)



def index(request):
     #return render(request, 'gatekeeper/home.html', {})
     return HttpResponseRedirect("/admin/gatekeeperapp/vehicle/add/")


@login_required
def piechart(request):
        vehicle = Vehicle.objects.all().order_by('-gatepass')
        print vehicle
        #context_dict = {'entries' : vehicle}
        gates = Gate.objects.all()
        ydata = []
        xdata = []
        for g in gates:
            vehicles_count = Vehicle.objects.filter(gate = g).count()
            ydata.append(vehicles_count)
            xdata.append(g.gate) 
#        xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
#        ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
        print "xd is ", xdata
        print ydata  
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "pieChart"
        chartcontainer = 'piechart_container'
        data = {
            'entries' : vehicle,
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
            }
        }
        return render(request, 'gatekeeper/piechart.html', data) 


@login_required  
def gentryin(request):
    liner = Liner.objects.all()
    vehicles = Vehicle.objects.all().count()
    vehicles_count = vehicles+1

    #vehicle = Vehicle.objects.all()
    vehicle = Vehicle.objects.latest('gatepass')
    print vehicle
    emp = Employee.objects.get(user = request.user)
    print "emp is ", emp 
    created_by = emp
    gate = emp.assigned_to
    gate_id = gate.id
    done = False
    if request.method == "POST":
        vehicle_form = VehicleForm(data=request.POST)
        container_form = ContainerForm(data=request.POST)
        #print "request post : ", request.POST
        if vehicle_form.is_valid():
            vehicle = vehicle_form.save()
            print "newly added vehicle is " , vehicle
            try:
                container_no_1 = request.POST['container_no_1']
                sz_1 = request.POST['sz_1']
                mty_1 = request.POST['mty_1']
                mfg_year_1 = request.POST['mfg_year_1']
                gr_weight_1 = request.POST['gr_weight_1']
                tare_weight_1 = request.POST['tare_weight_1']
                cbm_1 = request.POST['cbm_1']
                action_required_1 = request.POST['action_required_1']
                grade_1 = request.POST['grade_1']
                status_1 = request.POST['status_1']
                location_1 = request.POST['location_1']
                remarks_1 = request.POST['remarks_1']
                container_1 = Container.objects.create(vehicle = vehicle, remarks = remarks_1, location = location_1, status = status_1, grade = grade_1, action_required = action_required_1, cbm = cbm_1, tare_weight  = tare_weight_1, gr_weight = gr_weight_1, container_no = container_no_1, sz = sz_1, mty = mty_1, mfg_year = mfg_year_1) 
                
            except Argument, Exception:
                print "c errors"  
                print Argument, Exception
            try:
                container_no_2 = request.POST['container_no_2']
                sz_2 = request.POST['sz_2']
                mty_2 = request.POST['mty_2']
                mfg_year_2 = request.POST['mfg_year_2']
                gr_weight_2 = request.POST['gr_weight_2']
                tare_weight_2 = request.POST['tare_weight_2']
                cbm_2 = request.POST['cbm_2']
                action_required_2 = request.POST['action_required_2']
                grade_2 = request.POST['grade_2']
                status_2 = request.POST['status_2']
                location_2 = request.POST['location_2']
                remarks_2 = request.POST['remarks_2']
                container_2 = Container.objects.create(vehicle = vehicle, remarks = remarks_2, location = location_2, status = status_2, grade = grade_2, action_required = action_required_2, cbm = cbm_2, tare_weight  = tare_weight_2, gr_weight = gr_weight_2, container_no = container_no_2, sz = sz_2, mty = mty_2, mfg_year = mfg_year_2) 
                done = True
            except Argument, Exception:
                print "c errors"  
                print Argument, Exception
                
        else:
            print "verrors "
            print vehicle_form.errors
            
    else:
        vehicle_form = VehicleForm()
        container_form = ContainerForm()
    return render(request, 'gatekeeper/guard_entry.html',
     {'vehicle_form': vehicle_form, 'container_form':container_form, 'liner':liner, 'entries' : vehicle, 'vehicles_count':vehicles_count,
     'done': done, 'gate':gate, 'gate_id':gate_id})
     





@login_required  
def gentryout(request):
    liner = Liner.objects.all()
    vehicles = Vehicle.objects.all().count()
    vehicles_count = vehicles+1
    print "vs is ", vehicles_count
    vehicle = Vehicle.objects.all()
    emp = Employee.objects.get(user = request.user)
    print "emp is ", emp 
    created_by = emp
    gate = emp.assigned_to
    gate_id = gate.id
    done = False
    if request.method == "POST":
        vehicle_form = VehicleForm(data=request.POST)
        container_form = ContainerForm(data=request.POST)
        #print "request post : ", request.POST
        if vehicle_form.is_valid():
            vehicle = vehicle_form.save()
            print "newly added vehicle is " , vehicle
            try:
                container_no_1 = request.POST['container_no_1']
                sz_1 = request.POST['sz_1']
                mty_1 = request.POST['mty_1']
                mfg_year_1 = request.POST['mfg_year_1']
                gr_weight_1 = request.POST['gr_weight_1']
                tare_weight_1 = request.POST['tare_weight_1']
                cbm_1 = request.POST['cbm_1']
                action_required_1 = request.POST['action_required_1']
                grade_1 = request.POST['grade_1']
                status_1 = request.POST['status_1']
                location_1 = request.POST['location_1']
                remarks_1 = request.POST['remarks_1']
                container_1 = Container.objects.create(vehicle = vehicle, remarks = remarks_1, location = location_1, status = status_1, grade = grade_1, action_required = action_required_1, cbm = cbm_1, tare_weight  = tare_weight_1, gr_weight = gr_weight_1, container_no = container_no_1, sz = sz_1, mty = mty_1, mfg_year = mfg_year_1) 
                
            except Argument, Exception:
                print "c errors"  
                print Argument, Exception
            try:
                container_no_2 = request.POST['container_no_2']
                sz_2 = request.POST['sz_2']
                mty_2 = request.POST['mty_2']
                mfg_year_2 = request.POST['mfg_year_2']
                gr_weight_2 = request.POST['gr_weight_2']
                tare_weight_2 = request.POST['tare_weight_2']
                cbm_2 = request.POST['cbm_2']
                action_required_2 = request.POST['action_required_2']
                grade_2 = request.POST['grade_2']
                status_2 = request.POST['status_2']
                location_2 = request.POST['location_2']
                remarks_2 = request.POST['remarks_2']
                container_2 = Container.objects.create(vehicle = vehicle, remarks = remarks_2, location = location_2, status = status_2, grade = grade_2, action_required = action_required_2, cbm = cbm_2, tare_weight  = tare_weight_2, gr_weight = gr_weight_2, container_no = container_no_2, sz = sz_2, mty = mty_2, mfg_year = mfg_year_2) 
                done = True
            except Argument, Exception:
                print "c errors"  
                print Argument, Exception
                
        else:
            print "verrors "
            print vehicle_form.errors
            
    else:
        vehicle_form = VehicleForm()
        container_form = ContainerForm()
    return render(request, 'gatekeeper/guard_entry_out.html',
     {'vehicle_form': vehicle_form, 'container_form':container_form, 'liner':liner, 'entries' : vehicle, 'vehicles_count':vehicles_count,
     'done': done, 'gate':gate, 'gate_id':gate_id})



#@login_required

'''
def gateform(request):
    context = RequestContext(request)
    done = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        contact_form = EntryForm(data=request.POST)
        # If the two forms are valid...
        if contact_form.is_valid():
            # Save the user's form data to the database.
            feedback = contact_form.save()
            # Update our variable to tell the template
            # registration was successful.
            done = True
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print contact_form.errors
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        contact_form = EntryForm()
    # Render the template depending on the context.
    return render_to_response(
            'gatekeeper/home.html',
            {'contact_form': contact_form, 'done': done},
            context)
'''
	
@login_required  
def gate(request):
    
    vehicle = Vehicle.objects.all().order_by('-gatepass')
    context_dict = {'Vehicle' : vehicle}
    #return render(request, 'gatekeeper/report.html', context_dict)
    return HttpResponseRedirect("/admin/gatekeeperapp/vehicle/add/")

#class VehicleList(APIView):
#    def get(self, request, format=None):
#        vehicle = Vehicle.objects.all()
#        serialized = VehicleSerializer(vehicle, many=True)
#        return Response(serialized.data)
