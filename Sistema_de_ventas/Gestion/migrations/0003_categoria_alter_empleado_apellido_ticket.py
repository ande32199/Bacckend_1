# Generated by Django 5.1.5 on 2025-02-04 20:18

import Gestion.Validadores
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0002_alter_empleado_apellido_alter_empleado_cargo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'Categoria',
            },
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='Apellidos'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(5), Gestion.Validadores.validacion_numeros])),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('Abierto', 'Abierto'), ('En Proceso', 'En Proceso'), ('Cerrado', 'Cerrado')], default='Abierto', max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.empleado')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion.categoria')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'db_table': 'Ticket',
            },
        ),
    ]
