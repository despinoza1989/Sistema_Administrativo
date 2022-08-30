from django.urls import path
from .views import home, login, registro_cliente, registro, registro_profesional, listado_profesionales, listado_clientes, listado_administrativos
from .views import registro_administrativo, desactivar_usuario, activar_usuario, asignar_profesional, modificar_usuario
from .views import ListarUsuariosActivos, ListarUsuariosInactivos

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro_administrativo/', registro_administrativo, name="registro_administrativo"),
    path('listado_administrativos/', listado_administrativos, name="listado_administrativos"),
    path('registro_cliente/', registro_cliente, name="registro_cliente"),
    path('listado_clientes/', listado_clientes, name="listado_clientes"),
    path('registro_profesional/', registro_profesional, name="registro_profesional"),
    path('listado_profesionales/', listado_profesionales, name="listado_profesionales"),
    path('registro/', registro, name="registro"),
    path('usuarios-activos/', ListarUsuariosActivos.as_view(), name="usuarios_activos"),
    path('usuarios-inactivos/', ListarUsuariosInactivos.as_view(), name="usuarios_inactivos"),
    path('modificar-usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    path('desactivar-usuario/<id>/', desactivar_usuario, name="desactivar_usuario"), 
    path('activar-usuario/<id>/', activar_usuario, name="activar_usuario"), 
    path('activar-usuario/<id>/', activar_usuario, name="activar_usuario"), 
    path('asignar_profesional/', asignar_profesional, name="asignar_profesional"),




]
