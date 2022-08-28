from django.urls import path
from .views import home, login, registro_cliente, registro_profesional

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro_cliente/', registro_cliente, name="registro_cliente"),
    path('registro_profesional/', registro_profesional, name="registro_profesional"),
    
    
]
