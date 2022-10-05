from dataclasses import fields
from pyexpat import model
from tkinter.tix import Form
from django import forms
from myprint.models import *

class Order(forms.ModelForm):
    class Meta:
        models = Form
        fields = '__all__'


class UserRegisterModelForm(forms.ModelForm):

    
    # full_name= forms.CharField(max_length=64, widget=forms.TextInput(attrs={
    #     "class": 'form-control',
    #     'type': 'text',
    #     'placeholder': 'Полное имя'
    # }))
    # email= forms.EmailField(widget=forms.TextInput(attrs={
    #     "class": 'form-control',
    #     'type': 'number',
    #     'placeholder': 'Эл. адрес'
    # }))
    # phone_number= forms.IntegerField(widget=forms.TextInput(attrs={
    #     "class": 'form-control',
    #     'type': 'email',
    #     'placeholder': 'Телефонный номер'
    # }))
    # password= forms.CharField(widget=forms.TextInput(attrs={
    #     "class": 'form-control',
    #     'type': 'password',
    #     'placeholder': 'Пароль'
    # }))
    confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'password', 'confirm']
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }


class UserLoginForm(forms.Form):
    full_name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={
        "class": 'form-control mb-2',
        'type': 'number',
        'placeholder': 'Телефон ...'
    }))
    password = forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "class": 'form-control mb-5',
        'type': 'pasword',
        'placeholder': 'Пароль ...'
    }))
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }

class ResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']




