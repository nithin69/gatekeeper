from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User#, AbstractUser
from django.template.defaultfilters import slugify
from datetime import datetime




from gateuser.models import Employee

#from current_user import get_current_user


#import webcam #.admin  needed to show the right widget in the admin
#from webcam.fields import CameraField

 
#import webcam
#from webcam.fields import CameraField

class Liner(models.Model):
    liner = models.CharField(max_length=255, null=True, blank=True, verbose_name="Liner Name")
    def __unicode__(self):
        return self.liner  

class Transporter(models.Model):
    transporter_name = models.CharField(max_length=255, verbose_name="Transporter Name")
    
    def __unicode__(self):
        return self.transporter_name 

class Place(models.Model):
    place_from = models.CharField(max_length=255, verbose_name="Place From")
    
    def __unicode__(self):
        return self.place_from 
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Cha(models.Model):
    cha_shipper = models.CharField(max_length=255, verbose_name="Cha/Shipper")
    
    def __unicode__(self):
        return self.cha_shipper 

class Customer(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name="Customer Name")
    
    def __unicode__(self):
        return self.customer_name                         

class Gate(models.Model):
    gate = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return self.gate    

class Yard(models.Model):
    yard_name = models.CharField(max_length=255, null=True, blank=True)
    gate_name = models.ForeignKey(Gate)
    location =  models.CharField(max_length=255, null=True, blank=True)
    sub_location = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.yard_name    


class Seal(models.Model):
    line = models.ForeignKey(Liner, verbose_name="Liner", null=True, blank=True)
    prefix = models.CharField(max_length=20, null=True, blank=True)
    start_range = models.IntegerField()
    end_range = models.IntegerField()
    status = models.BooleanField(default=False)
    def __unicode__(self):
        return self.prefix    



class Vehicle(models.Model):
    movement_choices = (
        ('IN', 'IN'),
        ('OUT', 'OUT' ),
    )
    gate = models.ForeignKey(Gate, null=True, blank=True)
    gatepass = models.AutoField(primary_key=True)
    time_of_entry = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    line = models.ForeignKey(Liner, verbose_name="Liner", null=True, blank=True)
    customer_name = models.ForeignKey(Customer, null=True, blank=True, verbose_name="Customer Name")
    cha = models.ForeignKey(Cha, null=True, blank=True)
    #moment_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="liner Type")
    place_from = models.ForeignKey(Place, null=True, blank=True, verbose_name="Place From")
    vessel_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Vessel Name")
    vay_no =  models.CharField(max_length=255, null=True, blank=True, verbose_name="Vay. No.")
    transporter_name = models.ForeignKey(Transporter, null=True, blank=True, verbose_name="Transporter Name")
    vehicle_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="Truck No.")
    bill_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="BL No.")
    validity_date = models.DateField()
    movement_type = models.CharField(max_length=20, choices=movement_choices, null=True, blank=True)
    surveyor = models.CharField(max_length=255, null=True, blank=True)
    

    
    #pic = CameraField(upload_to='media', null=True, blank=True)
    
    
    def __unicode__(self):
        return self.vehicle_no
    def __str__(self):
        return str(self.gatepass)
    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
    #photo = CameraField('CameraPictureField', format='jpeg', null=True, blank=True)

    created_by = models.ForeignKey('gateuser.Employee', related_name='created_by', null = True, blank = True)
   
    '''
    def save(self, *args, **kwargs):
       request = kwargs.pop('request')
       emp = Employee.objects.get(user = request.user)
       print "emp is ", emp 
       self.created_by = emp
       self.gate = emp.assigned_to
       self.save()
       return obj 

    '''
    

'''
    created_by = models.ForeignKey(User, related_name='created_by', null = True, blank = True)
    def save(self, *args, **kwargs):
       if self.request:
       self.created_by = self.request.user
       self.save()
       return obj 
'''
    
    #transport = models.ForeignKey(Transport)

    
class Container(models.Model):
    action_choices = (
            ('CW', 'CW'),
            ('DS', 'DS'),
            ('DC', 'DC'),
            ('DW', 'DW'),
            ('HD', 'HD'),
            ('N/A', 'N/A'),
            ('SP', 'SP'),
            ('WW', 'WW'),
            ('3P', '3P')

    )
    status_choices = (
            ('AI', 'AI'),
            ('AP', 'AP'),
            ('AR', 'AR'),
            ('AV', 'AV'),
            ('EV', 'EV'),
            ('TTL', 'TTL')
            
    )

    grade_choices = (
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            
    )    
    vehicle = models.ForeignKey(Vehicle, verbose_name="Vehicle")
    container_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="Container No.")
    type_of_gate = models.CharField(max_length=255, null=True, blank=True, verbose_name="Movement Type of Container")
    sz = models.CharField(max_length=255, null=True, blank=True, verbose_name="Sz & Te")
    csc = models.CharField(max_length=255, null=True, blank=True, verbose_name="CSC Plate Details")
    mfg_year = models.CharField(max_length=255, null=True, blank=True, verbose_name="Mfg Year")    
    gr_weight = models.CharField(max_length=255, null=True, blank=True, verbose_name="Gr. Weight")
    tare_weight = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tare Weight")
    #cbm = models.CharField(max_length=255, null=True, blank=True, verbose_name="Cbm")
    set_temp = models.CharField(max_length=255, null=True, blank=True, verbose_name="Set Temp")
    ventilation = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ventilation")
    humidity = models.CharField(max_length=255, null=True, blank=True, verbose_name="Humidity")
    action_required = models.CharField(max_length=255, choices=action_choices, null=True, blank=True, verbose_name="Action Required")
    grade = models.CharField(max_length=255, choices=status_choices, null=True, blank=True, verbose_name="Grade")
    status = models.CharField(max_length=255, choices=status_choices, null=True, blank=True, verbose_name="Status")
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name="Location")
    remarks = models.CharField(max_length=255, null=True, blank=True, verbose_name="Remarks")
#    created_by = models.ForeignKey('auth.User')
#    created_by = models.ForeignKey(User, default=self.user)

#    def save(self, *args, **kwargs):
#       if self.request:
#	self.created_by = self.request.user
#	self.save()
#	return obj 
  
    def __unicode__(self):
        return self.container_no


class Docs(models.Model):
    order_no = models.CharField(max_length=255, null=True, blank=True)
    equipmentno = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    container_size = models.CharField(max_length=255, null=True, blank=True)
    container_type = models.CharField(max_length=255, null=True, blank=True)
    size_feet = models.CharField(max_length=255, null=True, blank=True)
    tareweight = models.CharField(max_length=255, null=True, blank=True)
    cargoweight = models.CharField(max_length=255, null=True, blank=True)
    pin = models.CharField(max_length=255, null=True, blank=True)
    interimpin = models.CharField(max_length=255, null=True, blank=True)
    properties = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)
    validity_port_date = models.CharField(max_length=255, null=True, blank=True)
    validity_port_time = models.CharField(max_length=255, null=True, blank=True)
    cntr_return_date = models.CharField(max_length=255, null=True, blank=True)
    cntr_return_time = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return self.equipmentno

