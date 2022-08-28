from django.urls import path
from .views import home, login, registro_cliente, registro_profesional, listado_profesionales, listado_clientes

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro_cliente/', registro_cliente, name="registro_cliente"),
    path('registro_profesional/', registro_profesional, name="registro_profesional"),
    path('profesionales_activos/', listado_profesionales, name="listado_profesional"),
    path('clientes_activos/', listado_clientes, name="listado_clientes"),
]
