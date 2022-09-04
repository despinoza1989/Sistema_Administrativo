from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ClienteForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Clientes, Personal
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'app/home.html')

#   REGISTROS

def registro_cliente(request):

    data = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Administrativo Registrado Exitosamente")
        else: 
            data["form"] = formulario

    return render(request, 'registration/registro_cliente.html',data)

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

def listado_clientes(request):
    clientes = Clientes.objects.all()

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


# MODIFICAR

def modificar_usuario(request, id):

    usuario = get_object_or_404(User, id=id)

    data = {
        'form': CustomUserCreationForm(instance=usuario)
    }

    if  request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario Modificado Correctamente")
            return redirect(to="usuarios_activos")
        data["form"] = formulario

    return render(request,'app/modificar/modificar_usuario.html', data)    