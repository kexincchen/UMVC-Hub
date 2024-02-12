# forms.py in your app directory
from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'pub_date', 'description', 'file']
