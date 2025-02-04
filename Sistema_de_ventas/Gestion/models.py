from django.db import models
from .choices import CARGO
from django.core.validators import MinValueValidator,MaxValueValidator, MaxLengthValidator, MinLengthValidator
from .Validadores import validacion_numeros


class Empleado(models.Model):
    id = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, verbose_name='Cambio')
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    cargo = models.CharField(max_length=50, choices=CARGO)

    class Meta:
        db_table = 'Empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre

