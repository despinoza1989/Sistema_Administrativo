from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Profesional, Cliente, Administrativo
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'app/home.html')

#   REGISTROS

def registro_administrativo(request):
    return render(request, 'registration/registro_administrativo.html')

def registro_cliente(request):
    return render(request, 'registration/registro_cliente.html')

def registro_profesional(request):
    return render(request, 'registration/registro_profesional.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)


#   LISTADOS

def listado_administrativos(request):
    administrativos = Administrativo.objects.all()

    data = {
        'administrativos': administrativos
    }
    return render(request, 'app/listar/listar_administrativo.html', data)


def listado_profesionales(request):
    profesionales = Profesional.objects.all()

    data = {
        'profesionales': profesionales
    }
    return render(request, 'app/listar/listar_profesional.html', data)


def listado_clientes(request):
    clientes = Cliente.objects.all()

    data = {
        'clientes': clientes
    }
    return render(request, 'app/listar/listar_cliente.html', data)

def listado_clientes(request):
    user = User.objects.all()

    data = {
        'user': user
    }
    return render(request, 'app/listar/listar_cliente.html', data)

class ListarUsuariosActivos(ListView):
    model = User
    template_name = 'app/listar/listar_usuarios_activos.html'
    queryset = User.objects.filter(is_active = True)

class ListarUsuariosInactivos(ListView):
    model = User
    template_name = 'app/listar/listar_usuarios_inactivos.html'
    queryset = User.objects.filter(is_active = False)



# ACTIVAR Y DESACTIVAR

def desactivar_usuario(request, id):

    usuario = get_object_or_404(User, id=id)
    usuario.is_active=False
    usuario.save()
    messages.success(request, "Usuario Desactivado Correctamente")
    return redirect(to="usuarios_activos")

def activar_usuario(request, id):

    usuario = get_object_or_404(User, id=id)
    usuario.is_active=True
    usuario.save()
    messages.success(request, "Usuario Activado Correctamente")
    return redirect(to="usuarios_inactivos")


# ASIGNAR  

def asignar_profesional(request):
    return render(request, 'app/asignar/asignar_profesional.html')