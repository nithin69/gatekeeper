from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from gateuser.models import Employee, Group
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import GroupAdmin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from gatekeeperapp.models import *

from checkboxselectmultiple.admin import CheckboxSelectMultipleAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class MyUserCreationForm(UserCreationForm):
    """
    A form that overrides the UserCreationForm
    """
    class Meta:
        model = User
        fields = ("username", "groups")


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    #GroupAdmin_inlines = list(GroupAdmin.inlines)
    
    inlines = (EmployeeInline, )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('groups',)}),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
)
    
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            for key, values in request.POST.lists():
                print(key, values)
            obj.first_name = request.POST['first_name']
            obj.last_name = request.POST['last_name']
            obj.email = request.POST['email']
            group_id = Group.objects.get(id = request.POST['groups'])
            print "enterg  group is  ", group_id 
            print dir(obj)
            obj.is_staff = True
            #obj.groups = group_id
            
            obj.save()
            obj.groups.add(group_id)
            obj.save()

# Re-register UserAdmin
UserAdmin.add_form = MyUserCreationForm
admin.site.register(User, UserAdmin)
admin.site.register(Group)
admin.site.register(Employee)
