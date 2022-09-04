from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Clientes

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email","password1", "password2"]

class ClienteForm(forms.ModelForm):

    class Meta: 
        model = Clientes

        fields = '__all__'
