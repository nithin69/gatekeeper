from django import forms
from registration.forms import RegistrationForm
from gateuser.models import Employee
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

