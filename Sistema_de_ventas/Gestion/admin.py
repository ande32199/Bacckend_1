from django.contrib import admin
from .models import Empleado, Categoria, Cliente, Producto

@admin.register (Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'apellido', 'direccion', 'telefono', 'email',  'cargo')
  search_fields = ('id', 'nombre', 'apellido')
  ist_filter = ('id', 'apellido')
@admin.register (Categoria)
class CategoriaAdmin(admin.ModelAdmin):
  list_display = ( 'nombre', 'descripcion')
  search_fields = ( 'nombre', 'descripcion')
  ist_filter = ('nombre')
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'apellido', 'direccion', 'telefono', 'email')
  search_fields = ('id', 'nombre', 'apellido')
  ist_filter = ('id', 'apellido')
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
  list_display = ('codigo','nombre','descripcion','precio','stock')
  search_fields = ('nombre', 'descripcion')
  list_filter = ('nombre', 'descripcion', 'precio')