from django.urls import path
from .views import home, login, registro_cliente, registro_profesional, listado_profesionales, listado_clientes, registro_administrativo


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro_administrativo/', registro_administrativo, name="registro_administrativo"),
    path('registro_cliente/', registro_cliente, name="registro_cliente"),
    path('registro_profesional/', registro_profesional, name="registro_profesional"),

]
