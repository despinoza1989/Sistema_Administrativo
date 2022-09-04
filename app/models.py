from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from django.db.models.query import QuerySet


# Create your models here.

TIPO_USUARIO= (
    ("Administrativo","Administrativo"),
    ("Profesional","Profesional"),
    )

GENERO= (
    ("1","Masculino"),
    ("2","Femenino"),
    ("3", "No Binario")
    )

ESTADO_CIVIL= (
    ("1","Casado(a)"),
    ("2","Soltero(a)"),
    ("3", "Viudo(a)"),
    ("4", "Divorciado(a)")
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

class Tipo_Usuario(models.Model):
    id_tipo_u = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO, default='')

    def __str__(self):
        return self.tipo_usuario

class Estado_Civil(models.Model):
    id_estado_c = models.AutoField(primary_key=True)
    tipo_estado_c = models.CharField(max_length=20, choices=ESTADO_CIVIL, default='')

    def __str__(self):
        return self.tipo_estado_c

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    tipo_genero = models.CharField(max_length=10, choices=GENERO, default='')

    def __str__(self):
        return self.tipo_genero

class Rubro(models.Model):
    id_rubro = models.AutoField(primary_key=True)
    tipo_rubro = models.CharField(max_length=200, choices=RUBRO, default='')

    def __str__(self):
        return self.tipo_rubro

class Personal(models.Model):
    id_administrativo = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10, default='')
    telefono_administrativo = models.IntegerField()
    nombre_administrativo = models.CharField(max_length=80, default='')
    apellidos_administrativo = models.CharField(max_length=80, default='')
    email_administrativo = models.CharField(max_length=100, default='')
    direccion_administrativo = models.CharField(max_length=200, default='')
    fecha_nacimiento = models.DateField()
    tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.PROTECT)
    estado_civil = models.ForeignKey(Estado_Civil, on_delete=models.PROTECT)
    sexo = models.ForeignKey(Genero, on_delete=models.PROTECT)

    def __str__(self):
        return self.rut


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=10, default='')    
    razon_socila = models.CharField(max_length=80, default='')
    telefono_cliente = models.IntegerField()
    email_cliente = models.CharField(max_length=200, default='')
    direccion_cliente = models.CharField(max_length=200, default='')
    rubro = models.ForeignKey(Rubro, on_delete=models.PROTECT)

    def __str__(self):
        return self.rol
