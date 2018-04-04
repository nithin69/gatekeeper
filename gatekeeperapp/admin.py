from django.contrib import admin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin import DateFieldListFilter
from import_export import resources
from django.template import RequestContext
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from gateuser import *
from django.contrib.admin import DateFieldListFilter
from gateuser.models import Employee
from daterange_filter.filter import DateRangeFilter
from django.contrib.auth.models import Group
from gatekeeperapp.forms import EntryForm
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

# Register your models here.

from .models import *
#from django.contrib.auth.models import Permission


'''
class EntryAdmin(admin.ModelAdmin):
    exclude = ('created_by', )
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
        return obj
    list_display = (
       'id', 'gate', 'vehicle', 'gatepass' , 'time_of_entry',  
       #'parentid',


    )
    
    #list_filter = ('added_on',)
    search_fields = ('id','gate',)
'''
class VehicleResource(resources.ModelResource):

 
    class Meta:
        model = Vehicle


class ContainerInline(admin.TabularInline):
    model = Container
    extra = 2


class ContainerAdmin(admin.ModelAdmin):
	list_display = ('container_no','status', 'sz','tare_weight')
	field = '__all__'


class LinerAdmin(admin.ModelAdmin):
    #list_display = ('liner')
    list_filter = ('liner',)
    field = '__all__'

class SealAdmin(admin.ModelAdmin):
    list_filter = ('line','prefix', 'start_range', 'end_range', 'status')
    field = '__all__'



class VehicleAdmin(ImportExportMixin, admin.ModelAdmin):
    	#list_display = ('gatepass')
	readonly_fields=('gatepass_id', 'time_of_entry')
  	resource_class = VehicleResource
	list_display = (
       	'gatepass', 'gate', 'vehicle_no',
    	)
        list_filter = (('time_of_entry', DateRangeFilter), ('line', RelatedDropdownFilter), ('gate', RelatedDropdownFilter), ('container', RelatedDropdownFilter), ('movement_type'))
        #list_filter = ('line', )
        field = ('gate', 'vehicle_no')
        search_fields = ['gatepass','customer_name__customer_name', 'line__liner', 'transporter_name__transporter_name', 'bill_no', ]
        list_filter = ('customer_name','line',)

        form = EntryForm
	
        def save_model(self, request, obj, form, change):
                emp = Employee.objects.get(user = request.user)
                print "emp is ", emp 
                obj.created_by = emp
           
                obj.gate = emp.assigned_to
                obj.save()
#                super().save_model(request, obj, form, change) 
 #               return obj 
        	
	def gatepass_id(self, obj):
		if obj.gatepass is None:
	            gatepass = Vehicle.objects.all().order_by('-gatepass')[:1]
        	    if gatepass:
			        return gatepass[0].gatepass + 2
        	    else:
			        return 1
        	else:
	    	    return obj.gatepass


    	


    	inlines = [ContainerInline]		

'''

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','type_user')
	field = '__all__'

'''

@login_required
def edi(request, *args, **kwargs):
    if 'liner' in request.GET:
        liner = request.GET['liner']
        print "liner n is", liner
	vehicle_resource = VehicleResource()
	liner_obj = Liner.objects.get(liner = liner)
	queryset = Vehicle.objects.filter(line=liner_obj)
	dataset = vehicle_resource.export(queryset)
	liner_2 = Liner.objects.all()
	print dataset.csv
	print "nithin"
	context_dict = {'entries' : liner_2}
	return render(request, 'gatekeeper/edi.html', context_dict)
    else:
        liner_2 = Liner.objects.all()
	context_dict = {'entries' : liner_2}
        return render(request, 'gatekeeper/edi.html', context_dict)


@login_required
def search(request, *args, **kwargs):
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


@login_required
def reports(request, *args, **kwargs):
    list_filter = ('time_of_entry',)
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user = user)
    designation = employee.designation    
   
    if designation == 'guard':

        vehicles = Vehicle.objects.all().order_by('-gatepass')
        containers = []
        cont = Container.objects.all()
        for v in vehicles: 
           cs = Container.objects.filter(vehicle = v,) 
           containers.append(cs) 
        elist = zip(vehicles, containers)
        context_dict = {'elist' : elist, 'entry' : cont}
        return render(request, 'gatekeeper/guard_report.html', context_dict)
    elif designation == 'manager' or designation == 'supervisor':
        liner = Liner.objects.all()
        vehicle = Vehicle.objects.all().order_by('-gatepass')
        #context_dict = {'entries' : vehicle}
        gates = Gate.objects.all()
        context_dict = {'liner':liner,'entries' : vehicle, 'gates' : gates}
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
        #return render(request, 'gatekeeper/piechart.html', data) 
        return render(request, 'gatekeeper/manager_report.html', context_dict)
   
        ''' 
        elif designation == 'supervisor':
	context = RequestContext(request)
	if 'from_date' in request.GET:
	        from_date = request.GET['from_date']
		if 'to_date' in request.GET:
	           to_date = request.GET['to_date']
        '''	
#	vehicle = Vehicle.objects.filter(from_date=from_date, to_date=to_date)
#        print vehicle


    
	
    vehicle = Vehicle.objects.all().order_by('-gatepass')
    context_dict = {'entries' : vehicle} 
    return render(request, 'gatekeeper/supervisor_report.html', context_dict)
#        return render(request, 'gatekeeper/supervisor_report.html', context)

    #else:

    #    context_dict = {} 
    #    return render(request, 'gatekeeper/error.html', context_dict)








admin.site.register_view('reports', view=reports)
#admin.site.register_view('search/', view=search)
#admin.site.register_view('edi/', view=edi)
admin.site.register(Gate)
admin.site.register(Transporter)
admin.site.register(Place)
admin.site.register(Cha)
admin.site.register(Yard)
admin.site.register(Customer)
admin.site.register(Liner, LinerAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
#admin.site.register(Permission)

#admin.site.register(CustomUser)
