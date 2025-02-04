from django.contrib import admin
from .models import Empleado, Categoria

@admin.register (Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'apellido', 'direccion', 'telefono', 'email',  'cargo')
  search_fields = ('cedula', 'nombre', 'apellido')
  ist_filter = ('cedula', 'apellido')
@admin.register (Categoria)
class CategoriaAdmin(admin.ModelAdmin):
  list_display = ( 'nombre', 'descripcion')
  search_fields = ( 'nombre', 'descripcion')
  ist_filter = ('nombre')
