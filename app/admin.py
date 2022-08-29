from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profesional, Cliente, Administrativo
# Register your models here.


admin.site.register(Administrativo)
admin.site.register(Profesional)
admin.site.register(Cliente)