from django.urls import path
<<<<<<< HEAD
from .views import home, login, registro_cliente, registro, registro_profesional, listado_profesionales, listado_clientes, registro_administrativo, desactivar_usuario, activar_usuario
from .views import ListarUsuariosActivos, ListarUsuariosInactivos
from .views import home, login, registro_cliente, registro, registro_profesional, listado_profesionales, listado_clientes, registro_administrativo

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro_administrativo/', registro_administrativo, name="registro_administrativo"),
    path('registro_cliente/', registro_cliente, name="registro_cliente"),
    path('registro_profesional/', registro_profesional, name="registro_profesional"),
    path('registro/', registro, name="registro"),

    path('usuarios-activos/', ListarUsuariosActivos.as_view(), name="usuarios_activos"),
    path('usuarios-inactivos/', ListarUsuariosInactivos.as_view(), name="usuarios_inactivos"),
    path('desactivar-usuario/<id>/', desactivar_usuario, name="desactivar_usuario"), 
    path('activar-usuario/<id>/', activar_usuario, name="activar_usuario"), 

]
