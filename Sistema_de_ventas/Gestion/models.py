from django.db import models
from .choices import CARGO, NOMBRE_CATEGORIA
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from .Validadores import validacion_numeros, validar_nombres, validar_telefono

class Empleado(models.Model):
    id = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, validators=[MaxLengthValidator(50), validar_nombres])
    apellido = models.CharField(max_length=50, verbose_name='Apellidos', validators=[MaxLengthValidator(50), validar_nombres])
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50, validators=[validacion_numeros])
    email = models.EmailField()
    cargo = models.CharField(max_length=50, choices=CARGO)

    class Meta:
        db_table = 'Empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, choices=NOMBRE_CATEGORIA)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Categoria'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, validators=[MaxLengthValidator(50), validar_nombres])
    apellido = models.CharField(max_length=50, validators=[MaxLengthValidator(50), validar_nombres])
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, validators=[validar_telefono])
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    stock = models.PositiveIntegerField(validators=[MinValueValidator(100)])
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='productos')

    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
