from django.contrib.auth.decorators import login_required
#from gateentry.forms import EntryForm
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from gateuser.models import Employee
from billing.models import Billing_rates
import random, json
import datetime
import time
from datetime import datetime, timedelta, time
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from django.core import serializers
#from rest_framework import generics
from django.db.models import Q
from django.views.generic.edit import FormView
import json
from django.http import HttpResponse
#from dal import autocomplete
import re
from django.utils import timezone
# Create your views here.


#admin/gatekeeperapp/vehicle/add/
@login_required  
def tvehicles(request):
    print "in tvvv"
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    vehicle = Vehicle.objects.filter(time_of_entry__range=[today_start, today_end])
    containers = Container.objects.filter(vehicle__time_of_entry__range=[today_start, today_end])
    context_dict = {'entries' : vehicle, 'containers' : containers,}
    return render(request, 'gatekeeper/tvehicles.html', context_dict)


@login_required  
def twohours(request):
    import datetime as x
    twohours = x.datetime.now() - timedelta(hours=2)
    print twohours
    vehicle = Vehicle.objects.filter(time_of_entry__gte=twohours)
    containers = Container.objects.filter(vehicle__time_of_entry__gte=twohours)
    context_dict = {'entries' : vehicle, 'containers' : containers,}
    return render(request, 'gatekeeper/twohours.html', context_dict)



@login_required  
def landing(request):
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user = user)
    designation = employee.designation
    context_dict = {}
#    return render(request, 'gatekeeper/landing.html', context_dict)
    if designation == 'guard':
        return render(request, 'gatekeeper/landing.html', context_dict)
    else:
        return HttpResponseRedirect("/admin/")

@login_required  
def report(request):
    
    context_dict = {}
    #return render(request, 'gatekeeper/report.html', context_dict)
    return render(request, 'gatekeeper/supervisor_report.html', context_dict)



@login_required
def search(request, *args, **kwargs):

    if 'from_date' in request.GET:
        from_date = request.GET['from_date']
        print "from date ", from_date
    if 'to_date' in request.GET:
        to_date = request.GET['to_date']    
    print "to date", to_date
    vehicle = Vehicle.objects.filter(time_of_entry__range=[from_date, to_date])
    containers = Container.objects.filter(vehicle__time_of_entry__range=[datetime.date.today().from_date, datetime.date.today().to_date])
    print vehicle
    context_dict = {'entries' : vehicle, 'containers' : containers}
    print "abbhh"
    return render(request, 'gatekeeper/supervisor_search_report.html', context_dict)

@login_required
def guardsearch(request, *args, **kwargs):
    import datetime as x
    if 'from_time' in request.GET:
        from_time = request.GET['from_time']
        print "from time ", from_time
    if 'to_time' in request.GET:
        to_time = request.GET['to_time']
        print "to time", to_time
    #today_min = datetime.date.combine(timezone.now().date(), datetime.time.from_time)
    #today_max = datetime.date.combine(timezone.now().date(), datetime.time.to_time)
    vehicle = Vehicle.objects.filter(time_of_entry__gte=[x.from_time,x.to_time])
    context_dict = {'elist' : vehicle}
    return render(request, 'gatekeeper/guard_report.html', context_dict)




@login_required
def managersearch(request, *args, **kwargs):
    #reporttype = request.GET['reporttype']
    #print reporttype
    liner = Liner.objects.all()
    gates = Gate.objects.all()
    momenttype = request.GET['momenttype']
    print "momenttype", momenttype
    print "nithin ecsdfas"
    if 'linertype' in request.GET:
        linertype = request.GET['linertype']
        print "linertype", linertype
    if 'from_date' in request.GET:
        from_date = request.GET['from_date']
        print from_date
    if 'to_date' in request.GET:
        to_date = request.GET['to_date']
        print to_date    
    



    if momenttype == "all" and linertype == "all":
        print "entered all view"
        vehicle = Vehicle.objects.filter(time_of_entry__range=[from_date, to_date])
              
    elif momenttype != "all" and linertype == "all":
        print "entered mt and lt"    
        vehicle = Vehicle.objects.filter(movement_type = momenttype, time_of_entry__range=[from_date, to_date])
    elif momenttype == "all" and linertype != "all":    
        print "entered mt and gt"
        vehicle = Vehicle.objects.filter(line = linertype, time_of_entry__range=[from_date, to_date])






    else:
        print "entered else"
        vehicle = Vehicle.objects.filter(movement_type = momenttype, line = linertype, time_of_entry__range=[from_date, to_date])
    print vehicle
    context_dict = {'entries' : vehicle, 'liner' : liner,}
    return render(request, 'gatekeeper/manager_report.html', context_dict)




def index(request):
     #return render(request, 'gatekeeper/home.html', {})
     return HttpResponseRedirect("/admin/gatekeeperapp/vehicle/add/")


@login_required
def piechart(request):
        print "in piicccc"
        movement_type = request.GET['momenttype']
        print "movement_type is " , movement_type
        linertype = Liner.objects.get(liner = request.GET['linertype'])
        gatetype = Gate.objects.get(gate = request.GET['gatetype']) # request.GET['gatetype']
        from_date = request.GET['from_date']
        to_date = request.GET['to_date']
        if movement_type == "ALL":
            vehicle = Vehicle.objects.filter(time_of_entry__range=[from_date, to_date]).order_by('-gatepass')
        else:
             vehicle = Vehicle.objects.filter(time_of_entry__range=[from_date, to_date], movement_type = movement_type).order_by('-gatepass')



        #context_dict = {'entries' : vehicle} line = linertype, gate = gatetype
        gates = Gate.objects.all()
        ydata = []
        xdata = []
        for g in gates:
            vehicles_count = Vehicle.objects.filter(time_of_entry__range=[from_date, to_date], movement_type = movement_type, line = linertype, gate = gatetype).count()
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
def piechartpage(request):
        liner = Liner.objects.all()
        containers = Container.objects.all().order_by('-id')
        vehicle = Vehicle.objects.all().order_by('-gatepass')
        #context_dict = {'entries' : vehicle}
        gates = Gate.objects.all()
        context_dict = {'liner':liner,'entries' : vehicle, 'gates' : gates, 'containers' : containers}
        ydata = []
        xdata = []
        for g in gates:
            vehicles_count = Vehicle.objects.filter(gate = g).count()
            ydata.append(vehicles_count)
            xdata.append(g.gate) 
#        xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
#        ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "pieChart"
        chartcontainer = 'piechart_container'
        data = {
            'containers' : containers,
            'liner' : liner,
            'entries' : vehicle,
            'gates' : gates,
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
    chas = Cha.objects.all()
    transporters = Transporter.objects.all()
    places = Place.objects.all()
    customers = Customer.objects.all()

    #vehicles = Vehicle.objects.all().count()
    #vehicles_count = vehicles+1
    container_1 = ""
    container_2 = ""
    #vehicle = Vehicle.objects.all()
    vehicles = Vehicle.objects.latest('gatepass')
    print "vehicles",vehicles
    gatepass_count = int(str(vehicles))+1 
    emp = Employee.objects.get(user = request.user)
    print "emp is ", emp 
    created_by = emp
    emp_id = emp.id
    gate = emp.assigned_to
    gate_id = gate.id
    yards = Yard.objects.get(gate_name_id = gate_id)
    print "yards",yards



    done = False
    container2present = False
    if request.method == "POST":
        vehicle_form = VehicleForm(data=request.POST)
        container_form = ContainerForm(data=request.POST)
        #print "request post : ", request.POST
        if vehicle_form.is_valid():
            vehicle = vehicle_form.save()
            print "newly added vehicle is " , vehicle
            try:
                print "entered try block"
                container_no_1 = request.POST['container_no_1']
                print "container_no_1", container_no_1
                docs = Docs.objects.get(equipmentno = container_no_1)
                print "docs", docs
                sz_1 = request.POST['sz_1']
                print "sz_1", sz_1
                mfg_year_1 = request.POST['mfg_year_1']
                print "mfg_year_1", mfg_year_1
                gr_weight_1 = request.POST['gr_weight_1']
                print "gr_weight_1", gr_weight_1
                tare_weight_1 = request.POST['tare_weight_1']
                print "tare_weight_1", tare_weight_1
                #cbm_1 = request.POST['cbm_1']
                action_required_1 = request.POST['action_required_1']
                print "action_required_1", action_required_1
                grade_1 = request.POST['grade_1']
                print "grade_1", grade_1
                status_1 = request.POST['status_1']
                print "status_1", status_1
                remarks_1 = request.POST['remarks_1']
                csc_1 = request.POST['csc_1']
                print " csc_1",csc_1
                type_of_gate_1 = request.POST['type_of_gate_1']

                surveyor = request.POST['surveyor']
                print "remarks_1", remarks_1
                print "vehicle", vehicle
                container_1 = Container.objects.create(vehicle = vehicle, type_of_gate = type_of_gate_1, csc = csc_1, remarks = remarks_1, status = status_1, grade = grade_1, action_required = action_required_1, tare_weight  = tare_weight_1, gr_weight = gr_weight_1, container_no = container_no_1, sz = sz_1, mfg_year = mfg_year_1) 
                print "container_1",container_1
                done = True
            except Exception,e:
                print "c1 errors"  
                print Exception, str(e)
            try :
                container_no_2 = request.POST['container_no_2']
                sz_2 = request.POST['sz_2']
                surveyor = request.POST['surveyor']
                mfg_year_2 = request.POST['mfg_year_2']
                gr_weight_2 = request.POST['gr_weight_2']
                tare_weight_2 = request.POST['tare_weight_2']
                #cbm_2 = request.POST['cbm_2']
                action_required_2 = request.POST['action_required_2']
                grade_2 = request.POST['grade_2']
                status_2 = request.POST['status_2']
                csc_2 = request.POST['csc_2']
                type_of_gate_2 = request.POST['type_of_gate_2']
                remarks_2 = request.POST['remarks_2']

                if container_no_2 == "" or sz_2 == "":
                    container_2 = "null"
                    container2present = False
                    print " in c2p null"   

                else:
                    container_2 = Container.objects.create(vehicle = vehicle,type_of_gate = type_of_gate_2, csc = csc_2, remarks = remarks_2, status = status_2, grade = grade_2, action_required = action_required_2, tare_weight  = tare_weight_2, gr_weight = gr_weight_2, container_no = container_no_2, sz = sz_2, mfg_year = mfg_year_2) 
                    done = True
                    container2present = True
            except Exception,e: 
                print "in exept...."
                print Exception, str(e)

                
        else:
            print "verrors "
            print vehicle_form.errors
            
    else:
        vehicle_form = VehicleForm()
        container_form = ContainerForm()
    print "final c2p is " , container2present , done
    print "vehicles  - ", vehicles.time_of_entry , "  -  " , vehicles.bill_no , "  -  "
    return render(request, 'gatekeeper/guard_entry.html',
     {'vehicle_form': vehicle_form, 'container_form':container_form, 'liner':liner, 'entries' : vehicles, 'container_1' : container_1 , 'container_2' : container_2, 'done': done, 'gate':gate, 'gate_id':gate_id,'container2present': container2present,
        'chas': chas, 'transporters': transporters,'emp_id':emp_id , 'gate_id':gate_id,'gatepass_count' : gatepass_count, 'places' : places, 'customers' : customers, 'yards':yards})
     

@login_required  
def gentryout(request):
    liner = Liner.objects.all()
    chas = Cha.objects.all()
    transporters = Transporter.objects.all()

    places = Place.objects.all()
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all().count()
    vehicles_count = vehicles+1
    print "vs is ", vehicles_count
    vehicle = Vehicle.objects.all()
    container_1 = ""
    container_2 = ""
    emp = Employee.objects.get(user = request.user)
    print "emp is ", emp 
    created_by = emp
    gate = emp.assigned_to
    gate_id = gate.id
    yards = Yard.objects.filter(gate_name_id = gate_id)
    gatepass_count = int(str(vehicles))+1 
    done = False
    container2present = False
    if request.method == "POST":
        vehicle_form = VehicleForm(data=request.POST)
        container_form = ContainerForm(data=request.POST)
        #print "request post : ", request.POST
        if vehicle_form.is_valid():
            vehicle = vehicle_form.save()
            print "newly added vehicle is " , vehicle
            try:
                print "gateout entered"
                container_no_1 = request.POST['container_no_1']
                print "cn_1 is ", container_no_1
                sz_1 = request.POST['sz_1']
                print "sz_1 is ", sz_1
                #mty_1 = request.POST['mty_1']
                #print "cn_1 is ", container_no_1
                mfg_year_1 = request.POST['mfg_year_1']
                print "mfg_year_1 is ", mfg_year_1
                gr_weight_1 = request.POST['gr_weight_1']
                print "gr_weight_1 is ", gr_weight_1
                tare_weight_1 = request.POST['tare_weight_1']
                print "tare_weight_1 is ", tare_weight_1
                #cbm_1 = request.POST['cbm_1']
                temperature_1 = request.POST['temperature_1']
                print "temperature_1 is ", temperature_1
                humidity_1 = request.POST['humidity_1']
                print "humidity_1 is ", humidity_1
                ventilation_1 = request.POST['ventilation_1']
                print "ventilation_1 is ", ventilation_1
                #action_required_1 = request.POST['action_required_1']
                #print "action_required_1 is ", action_required_1
                grade_1 = request.POST['grade_1']
                print "grade_1 is ", grade_1
                status_1 = request.POST['status_1']
                print "status_1 is ", status_1
                csc_1 = request.POST['csc_1']
                remarks_1 = request.POST['remarks_1']
                type_of_gate_1 = request.POST['type_of_gate_1']
                print "remarks_1 ", remarks_1
                container_1 = Container.objects.create(vehicle = vehicle, remarks = remarks_1,csc= csc_1, type_of_gate = type_of_gate_1, status = status_1, grade = grade_1, tare_weight  = tare_weight_1, 
                    gr_weight = gr_weight_1, container_no = container_no_1, sz = sz_1,  
                    mfg_year = mfg_year_1,) 
                print "container_1 added succ", container_1
                done = True

            except Exception as e:
                print "c errors c1"  
                print e.message
            try:
                container_no_2 = request.POST['container_no_2']
                sz_2 = request.POST['sz_2']
                #mty_2 = request.POST['mty_2']
                mfg_year_2 = request.POST['mfg_year_2']
                gr_weight_2 = request.POST['gr_weight_2']
                tare_weight_2 = request.POST['tare_weight_2']
                #cbm_2 = request.POST['cbm_2']
                temperature_2 = request.POST['temperature_2']
                humidity_2 = request.POST['humidity_2']
                ventilation_2 = request.POST['ventilation_2']
                #action_required_2 = request.POST['action_required_2']
                grade_2 = request.POST['grade_2']
                status_2 = request.POST['status_2']
                csc_2 = request.POST['csc_2']
                remarks_2 = request.POST['remarks_2']

                if container_no_2 == "" or sz_2 == "":
                    container_2 = "null"
                    container2present = False
                    print " in c2p null"   

                else:
                    container_2 = Container.objects.create(vehicle = vehicle, csc= csc_2, remarks = remarks_2, status = status_2, grade = grade_2, tare_weight  = tare_weight_2, gr_weight = gr_weight_2, container_no = container_no_2, sz = sz_2, mfg_year = mfg_year_2,
                    set_temp = temperature_2,humidity_2 = humidity_2,ventilation = ventilation_2) 
                    done = True
                    container2present = True



                
                
            except Exception as e:
                print "c errors"  
                print e.message
                
        else:
            print "verrors "
            print vehicle_form.errors
            
    else:
        vehicle_form = VehicleForm()
        container_form = ContainerForm()
    print "cp ion s ",  container2present
    return render(request, 'gatekeeper/guard_entry_out.html',
     {'vehicle_form': vehicle_form, 'container_form':container_form, 'liner':liner, 'entries' : vehicle, 'vehicles_count':vehicles_count, 'container_1' : container_1 , 'container_2' : container_2, 
     'done': done, 'gate':gate, 'gate_id':gate_id,'gatepass_count' : gatepass_count, 'container2present': container2present, 'chas': chas, 'transporters': transporters, 'places' : places, 'customers' : customers, 'yards' : yards})



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


class AutoCompleteView(FormView):
    def get(self,request,*args,**kwargs):
        print "entered into the AutoCompleteView"
        data = request.GET
        containers = data.get("container_id")

        print "containers",containers
        if containers:
            container = Docs.objects.get(equipmentno = containers)
            print "containers 2",containers
        else:
            pass
        results = []
        c_json = {}
        c_json['id'] = container.id
        c_json['sz'] = container.size
        c_json['tare_weight'] = container.tareweight
        c_json['validity_date'] = container.validity_port_date
        c_json['order_no'] = container.order_no
        c_json['container_type'] = container.container_type
        results.append(c_json)
        data = json.dumps(results)
        #data = data[2:-2]
        #data = data.replace('"', '')
        print "data", data
        li = list(re.split('[,:]', data))
        print "li", li 
        size = li[1] #[:4]
        mimetype = 'application/json'
        print "size is ", size
        return HttpResponse(data, content_type='application/json')

class AutoCompleteOut(FormView):
    def get(self,request,*args,**kwargs):
        print "entered into the AutoCompleteView"
        data = request.GET
        containers = data.get("container_id")

        print "containers",containers
        if containers:
            container = Container.objects.get(container_no = containers)

            print "containers 2",containers
        else:
            pass
        results = []
        c_json = {}
        c_json['id'] = container.id
        c_json['sz'] = container.sz
        c_json['tare_weight'] = container.tare_weight
        c_json['mfg_year'] = container.mfg_year
        c_json['gr_weight'] = container.gr_weight
        c_json['csc'] = container.csc
        #c_json['order_no'] = container.order_no
        #c_json['container_type'] = container.container_type
        results.append(c_json)
        data = json.dumps(results)
        #data = data[2:-2]
        #data = data.replace('"', '')
        print "data", data
        
        #size = li[1] #[:4]
        mimetype = 'application/json'
        
        return HttpResponse(data, content_type='application/json')


class AutoCompleteCharges(FormView):
    def get(self,request,*args,**kwargs):
        print "entered into the AutoCompleteCharges"
        data = request.GET
        liner_val = data.get("liner_val")
        place_val = data.get("place_from_val")
        gate_val = data.get("gate_val")
        
        liner = Liner.objects.get(id = liner_val)
        place = Place.objects.get(id = place_val)
        gate = Gate.objects.get(id = gate_val) # request.GET['gatetype']
        print "g val - ", liner , "  - " ,  place , "  - ", gate
        rates = Billing_rates.objects.get(location_name = place, liner_name = liner, gate_name = gate)
        results = []
        #results.append(rates)
        #data = json.dumps(rates)
        print rates.toJSON()
        return HttpResponse(rates.toJSON(), content_type='application/json')        