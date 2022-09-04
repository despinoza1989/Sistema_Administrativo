from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Personal, Clientes
# Register your models here.


admin.site.register(Personal)
admin.site.register(Clientes)