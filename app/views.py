from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profesional, Cliente

# Create your views here.


def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'app/home.html')

def registro_cliente(request):
    return render(request, 'registration/registro_cliente.html')

def registro_profesional(request):
    return render(request, 'registration/registro_profesional.html')

def listado_profesionales(request):
    profesionales = Profesional.objects.all()

    data = {
        'profesionales': profesionales
    }
    return render(request, 'app/listar/listar_profesional_activos.html', data)

def listado_clientes(request):
    clientes = Cliente.objects.all()

    data = {
        'clientes': clientes
    }
    return render(request, 'app/listar/listar_cliente_activos.html', data)
