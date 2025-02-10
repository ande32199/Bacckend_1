from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, CategoriaViewSet, ClienteViewSet, ProductoViewSet

# Crea un router y registra las vistas
router = DefaultRouter()
router.register(r'Empleados', EmpleadoViewSet)
router.register(r'Categoria', CategoriaViewSet)
router.register(r'Cliente', ClienteViewSet)
router.register(r'Producto', ProductoViewSet)
# Define las URLs de la API
urlpatterns = [
    path('', include(router.urls)),
]
