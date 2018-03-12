from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib import admin
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

from django.contrib.auth.models import Group


        
class Employee(models.Model):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    designation_choices = (
        ('guard', 'GUARD'),
        ('supervisor', 'SUPERVISOR' ),
        ('manager', 'MANAGER' ),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(_('designation'),choices=designation_choices, max_length=20)
    assigned_to = models.ForeignKey('gatekeeperapp.Gate', related_name="guard_gate", blank = True, null = True)

    
    def __unicode__(self):
        return unicode(self.user)

    
class Group(Group):
    pass

    class Meta:
        app_label = 'authentication'
