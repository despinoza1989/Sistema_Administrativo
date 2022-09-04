from django.urls import path
from .views import home, login, registro_cliente, registro, listado_clientes
from .views import desactivar_usuario, activar_usuario, asignar_profesional, modificar_usuario
from .views import ListarUsuariosActivos, ListarUsuariosInactivos

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro_cliente/', registro_cliente, name="registro_cliente"),
    path('listado_clientes/', listado_clientes, name="listado_clientes"),
    path('registro/', registro, name="registro"),
    path('usuarios-activos/', ListarUsuariosActivos.as_view(), name="usuarios_activos"),
    path('usuarios-inactivos/', ListarUsuariosInactivos.as_view(), name="usuarios_inactivos"),
    path('modificar-usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    path('desactivar-usuario/<id>/', desactivar_usuario, name="desactivar_usuario"), 
    path('activar-usuario/<id>/', activar_usuario, name="activar_usuario"), 
    path('activar-usuario/<id>/', activar_usuario, name="activar_usuario"), 
    path('asignar_profesional/', asignar_profesional, name="asignar_profesional"),

]
