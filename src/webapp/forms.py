# forms.py in your app directory
# from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ["name", "pub_date", "description", "file"]


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
