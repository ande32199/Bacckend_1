from django.contrib import admin
from .models import Empleado

@admin.register (Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'apellido', 'direccion', 'telefono', 'email',  'cargo')
  search_fields = ('cedula', 'nombre', 'apellido')
  ist_filter = ('cedula', 'apellido')
