from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Administrativo, Profesional, Cliente

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email","password1", "password2"]

class AdministrativoForm(forms.ModelForm):

    class Meta: 
        model = Administrativo

        fields = '__all__'

class ClienteForm(forms.ModelForm):

    class Meta: 
        model = Cliente

        fields = '__all__'

class ProfesionalForm(forms.ModelForm):

    class Meta: 
        model = Profesional

        fields = '__all__'