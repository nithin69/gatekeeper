__author__ = 'puppig1'

from django import forms
from .models import *
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from django.contrib.auth.models import User, Group, Permission
#from gatekeeperapp.models import Entry
from checkboxselectmultiple.widgets import CheckboxSelectMultiple

class EntryForm(forms.ModelForm):

    ''' 
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        del self.fields['created_by']
    '''

    class Meta:
        model = Vehicle
        fields = ('line', 'gatepass', 'movement_type', 'place_from', 'bill_no', 'validity_date', 'customer_name', 'cha', 'vessel_name', 'vay_no', 'transporter_name', 'vehicle_no',)
        #fields = '__all__' 


class GateForm(forms.ModelForm):

	class Meta:
		model = Gate
		fields = '__all__'

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'

class ContainerForm(forms.ModelForm):

    class Meta:
        model = Container
        fields = '__all__'

class DocsForm(forms.Form):
    class Meta:
        model = Docs
        fields = ("size")