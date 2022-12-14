# Generated by Django 4.1 on 2022-09-04 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(default='', max_length=10)),
                ('razon_socila', models.CharField(default='', max_length=80)),
                ('telefono_cliente', models.IntegerField()),
                ('email_cliente', models.CharField(default='', max_length=200)),
                ('direccion_cliente', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Civil',
            fields=[
                ('id_estado_c', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estado_c', models.CharField(choices=[('1', 'Casado(a)'), ('2', 'Soltero(a)'), ('3', 'Viudo(a)'), ('4', 'Divorciado(a)')], default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_genero', models.CharField(choices=[('1', 'Masculino'), ('2', 'Femenino'), ('3', 'No Binario')], default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id_administrativo', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(default='', max_length=10)),
                ('telefono_administrativo', models.IntegerField()),
                ('nombre_administrativo', models.CharField(default='', max_length=80)),
                ('apellidos_administrativo', models.CharField(default='', max_length=80)),
                ('email_administrativo', models.CharField(default='', max_length=100)),
                ('direccion_administrativo', models.CharField(default='', max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.estado_civil')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id_rubro', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_rubro', models.CharField(choices=[('NO APLICA', 'NO APLICA'), ('AGRICULTURA, GANADER??A, SILVICULTURA Y PESCA', 'AGRICULTURA, GANADER??A, SILVICULTURA Y PESCA'), ('EXPLOTACI??N DE MINAS Y CANTERAS', 'EXPLOTACI??N DE MINAS Y CANTERAS'), ('INDUSTRIA MANUFACTURERA', 'INDUSTRIA MANUFACTURERA'), ('SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO', 'SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO'), ('SUMINISTRO DE AGUA; EVACUACI??N DE AGUAS RESIDUALES, GESTI??N DE DESECHOS Y DESCONTAMINACI??N', 'SUMINISTRO DE AGUA; EVACUACI??N DE AGUAS RESIDUALES, GESTI??N DE DESECHOS Y DESCONTAMINACI??N'), ('CONSTRUCCI??N', 'CONSTRUCCI??N'), ('COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACI??N DE VEHICULOS AUTOMOTORES Y MOTOCICLETAS', 'COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACI??N DE VEHICULOS AUTOMOTORES Y MOTOCICLETAS'), ('TRANSPORTE Y ALMACENAMIENTO', 'TRANSPORTE Y ALMACENAMIENTO'), ('ACTIVIDADES DE ALOJAMIENTO Y DE SERVICIO DE COMIDAS', 'ACTIVIDADES DE ALOJAMIENTO Y DE SERVICIO DE COMIDAS'), ('INFORMACI??N Y COMUNICACIONES', 'INFORMACI??N Y COMUNICACIONES'), ('ACTIVIDADES FINANCIERAS Y DE SEGUROS', 'ACTIVIDADES FINANCIERAS Y DE SEGUROS'), ('ACTIVIDADES INMOBILIARIAS', 'ACTIVIDADES INMOBILIARIAS'), ('ACTIVIDADES PROFESIONALES, CIENTIFICAS Y T??CNICAS', 'ACTIVIDADES PROFESIONALES, CIENTIFICAS Y T??CNICAS'), ('ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO', 'ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO'), ('ADMINISTRACI??N P??BLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACI??N OBLIGATORIA', 'ADMINISTRACI??N P??BLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACI??N OBLIGATORIA'), ('ENSE??ANZA', 'ENSE??ANZA'), ('ACTIVIDADES DE ATENCI??N DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL', 'ACTIVIDADES DE ATENCI??N DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL'), ('ACTIVIDADES ART??STICAS, DE ENTRETENIMIENTO Y RECREATIVAS', 'ACTIVIDADES ART??STICAS, DE ENTRETENIMIENTO Y RECREATIVAS'), ('OTRAS ACTIVIDADES DE SERVICIOS', 'OTRAS ACTIVIDADES DE SERVICIOS'), ('ACTIVIDADES DE LOS HOGARES COMO EMPLEADORES; ACTIVIDADES NO DIFERENCIADAS DE LOS HOGARES', 'ACTIVIDADES DE LOS HOGARES COMO EMPLEADORES; ACTIVIDADES NO DIFERENCIADAS DE LOS HOGARES'), ('ACTIVIDADES DE ORGANIZACIONES Y ??RGANOS EXTRATERRITORIALES', 'ACTIVIDADES DE ORGANIZACIONES Y ??RGANOS EXTRATERRITORIALES')], default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('id_tipo_u', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_usuario', models.CharField(choices=[('Administrativo', 'Administrativo'), ('Profesional', 'Profesional')], default='', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Profesional',
        ),
        migrations.AddField(
            model_name='personal',
            name='tipo_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_usuario'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='rubro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.rubro'),
        ),
    ]
