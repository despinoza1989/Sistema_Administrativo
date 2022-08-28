from django.urls import path
from .views import home, login, registro_cliente

urlpatterns = [
    path('', home, name="home"),
    path('', login, name="login"),
    path('registro_cliente/', registro_cliente, name="registro_cliente"),
    
    
]
