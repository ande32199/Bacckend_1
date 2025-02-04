from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet

# Crea un router y registra las vistas
router = DefaultRouter()
router.register(r'Empleados', EmpleadoViewSet)

# Define las URLs de la API
urlpatterns = [
    path('', include(router.urls)),
]
