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


class Gate(models.Model):
    gate = models.CharField(max_length=255, null=True, blank=True)
    
    def __unicode__(self):
        return self.gate    


'''
class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('guard', 'Guard'),
        ('manager', 'Manager' ),
        ('supervisor', 'Supervisor' ),
    )
    user = models.OneToOneField(User)
    #gate = models.ForeignKey(Gate, null=True, blank=True)
    type_user = models.CharField(max_length=20, default='guard',choices=USER_TYPE_CHOICES)
    def __unicode__(self):
        return unicode(self.user)
'''

'''
class Transport(models.Model):
    transporter_name = models.CharField(max_length=255, null=True, blank=True)
    customer_name = models.CharField(max_length=255, null=True, blank=True) 
    def __unicode__(self):
        return self.transporter_name

'''

class Vehicle(models.Model):
    movement_choices = (
        ('IN', 'IN'),
        ('OUT', 'OUT' ),
    )
    gate = models.ForeignKey(Gate, null=True, blank=True)
    gatepass = models.AutoField(primary_key=True)
    time_of_entry = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    line = models.ForeignKey(Liner, verbose_name="Liner", null=True, blank=True)
    customer_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Customer Name")
    cha = models.CharField(max_length=255, null=True, blank=True, verbose_name="CHA/Shipper")
    #moment_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="liner Type")
    place_from = models.CharField(max_length=255, null=True, blank=True, verbose_name="Place From")
    vessel_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Vessel Name")
    vay_no =  models.CharField(max_length=255, null=True, blank=True, verbose_name="Vay. No.")
    transporter_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Transporter Name")
    vehicle_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="Truck No.")
    bill_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="BL No.")
    validity_date = models.DateField()
    movement_type = models.CharField(max_length=20, choices=movement_choices, null=True, blank=True)
    

    
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
    vehicle = models.ForeignKey(Vehicle, verbose_name="Vehicle")
    container_no = models.CharField(max_length=255, null=True, blank=True, verbose_name="Container No.")

    sz = models.CharField(max_length=255, null=True, blank=True, verbose_name="Sz & Te")
    mty = models.CharField(max_length=255, null=True, blank=True, verbose_name="Mty / Ldn")
    mfg_year = models.CharField(max_length=255, null=True, blank=True, verbose_name="Mfg Year")    
    gr_weight = models.CharField(max_length=255, null=True, blank=True, verbose_name="Gr. Weight")
    tare_weight = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tare Weight")
    cbm = models.CharField(max_length=255, null=True, blank=True, verbose_name="Cbm")
    action_required = models.CharField(max_length=255, null=True, blank=True, verbose_name="Action Required")
    grade = models.CharField(max_length=255, null=True, blank=True, verbose_name="Grade")
    status = models.CharField(max_length=255, null=True, blank=True, verbose_name="Status")
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

'''
class Entry(models.Model):
    gate = models.ForeignKey(Gate)
    vehicle = models.ForeignKey(Vehicle)
    gatepass = models.CharField(max_length=255, null=True, blank=True)
    time_of_entry = models.DateTimeField(default=datetime.now)
    moment_type = models.CharField(max_length=255, null=True, blank=True)
    place_from = models.CharField(max_length=255, null=True, blank=True)
    bill_no = models.CharField(max_length=255, null=True, blank=True)
    validity_date = models.DateTimeField()
    action_required = models.TextField(null=True, blank=True)
    #photo = CameraField('CameraPictureField', format='jpeg', null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='created_by', null = True, blank = True)

     
    def save(self, *args, **kwargs):
       if self.request:
	   self.created_by = self.request.user
       self.save()
       return obj 
    
    def __unicode__(self):
        return unicode(self.gatepass)
    
'''


