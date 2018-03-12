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


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from gatekeeperapp.models import *

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )


# Re-register UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Group)
