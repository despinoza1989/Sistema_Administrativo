from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from django.db.models.query import QuerySet


# Create your models here.

TIPO= (
    ("Administrativo","Administrativo"),
    ("Profesional","Profesional"),
    ("Cliente", "Cliente")
    )

SEXO= (
    ("Masculino","Masculino"),
    ("Femenino","Femenino"),
    ("No Binario", "No Binario")
    )

ESTADO_CIVIL= (
    ("Casado","Casado"),
    ("Soltero","Soltero"),
    ("Viudo", "Viudo"),
    ("Divorciado", "Divorciado")
    )

RUBRO= (
    ("NO APLICA","NO APLICA"),
    ("AGRICULTURA, GANADERÍA, SILVICULTURA Y PESCA","AGRICULTURA, GANADERÍA, SILVICULTURA Y PESCA"), 
    ("EXPLOTACIÓN DE MINAS Y CANTERAS","EXPLOTACIÓN DE MINAS Y CANTERAS"),
    ("INDUSTRIA MANUFACTURERA","INDUSTRIA MANUFACTURERA"),
    ("SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO","SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO"),
    ("SUMINISTRO DE AGUA; EVACUACIÓN DE AGUAS RESIDUALES, GESTIÓN DE DESECHOS Y DESCONTAMINACIÓN","SUMINISTRO DE AGUA; EVACUACIÓN DE AGUAS RESIDUALES, GESTIÓN DE DESECHOS Y DESCONTAMINACIÓN"),
    ("CONSTRUCCIÓN","CONSTRUCCIÓN"),
    ("COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACIÓN DE VEHICULOS AUTOMOTORES Y MOTOCICLETAS","COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACIÓN DE VEHICULOS AUTOMOTORES Y MOTOCICLETAS"),
    ("TRANSPORTE Y ALMACENAMIENTO","TRANSPORTE Y ALMACENAMIENTO"),
    ("ACTIVIDADES DE ALOJAMIENTO Y DE SERVICIO DE COMIDAS","ACTIVIDADES DE ALOJAMIENTO Y DE SERVICIO DE COMIDAS"),
    ("INFORMACIÓN Y COMUNICACIONES","INFORMACIÓN Y COMUNICACIONES"),
    ("ACTIVIDADES FINANCIERAS Y DE SEGUROS","ACTIVIDADES FINANCIERAS Y DE SEGUROS"),
    ("ACTIVIDADES INMOBILIARIAS","ACTIVIDADES INMOBILIARIAS"),
    ("ACTIVIDADES PROFESIONALES, CIENTIFICAS Y TÉCNICAS","ACTIVIDADES PROFESIONALES, CIENTIFICAS Y TÉCNICAS"),
    ("ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO","ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO"),
    ("ADMINISTRACIÓN PÚBLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACIÓN OBLIGATORIA","ADMINISTRACIÓN PÚBLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACIÓN OBLIGATORIA"),
    ("ENSEÑANZA","ENSEÑANZA"),
    ("ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL","ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL"),
    ("ACTIVIDADES ARTÍSTICAS, DE ENTRETENIMIENTO Y RECREATIVAS","ACTIVIDADES ARTÍSTICAS, DE ENTRETENIMIENTO Y RECREATIVAS"),
    ("OTRAS ACTIVIDADES DE SERVICIOS","OTRAS ACTIVIDADES DE SERVICIOS"),
    ("ACTIVIDADES DE LOS HOGARES COMO EMPLEADORES; ACTIVIDADES NO DIFERENCIADAS DE LOS HOGARES","ACTIVIDADES DE LOS HOGARES COMO EMPLEADORES; ACTIVIDADES NO DIFERENCIADAS DE LOS HOGARES"),
    ("ACTIVIDADES DE ORGANIZACIONES Y ÓRGANOS EXTRATERRITORIALES","ACTIVIDADES DE ORGANIZACIONES Y ÓRGANOS EXTRATERRITORIALES"),
    )

class Profesional(models.Model):
    id_profesional = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10, default='')
    telefono_profesional = models.IntegerField()
    nombre_profesional = models.CharField(max_length=80, default='')
    apellidos_profesional = models.CharField(max_length=80, default='')
    email_profesional = models.CharField(max_length=100, default='')
    direccion_profesional = models.CharField(max_length=200, default='')
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=200, choices=ESTADO_CIVIL, default='')
    sexo = models.CharField(max_length=10, choices=SEXO, default='')

    def __str__(self):
        return self.rut

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=10, default='')
    rubro = models.CharField(max_length=90, choices=RUBRO, default='')
    razon_socila = models.CharField(max_length=80, default='')
    telefono_cliente = models.IntegerField()
    email_cliente = models.CharField(max_length=200, default='')
    direccion_cliente = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.rol
