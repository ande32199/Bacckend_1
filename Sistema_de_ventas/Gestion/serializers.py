from rest_framework import serializers
from.models import Empleado, Categoria, Cliente, Producto

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
class ProductoSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'