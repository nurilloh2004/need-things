from dataclasses import fields
from operator import mod
from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        models = Form
        fields = ['full_name', 'phone_number']
        