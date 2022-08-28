from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def registro_cliente(request):
    return render(request, 'registration/registro_cliente.html')

def registro_profesional(request):
    return render(request, 'registration/registro_profesional.html')