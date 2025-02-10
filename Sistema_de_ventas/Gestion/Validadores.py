import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
def validacion_numeros(value):
    if not value.isdigit():
        raise ValidationError("El valor debe contener solo números") 
def validacion_numeros(value):
    if not value.isdigit():
        raise ValidationError('El ID debe contener solo números.')

def validar_nombres(value):
    if not value.isalpha():
        raise ValidationError("El nombre solo puede contener letras.")

def validar_telefono(value):
    if not re.match(r'^\+?\d{7,15}$', value):
        raise ValidationError('El número de teléfono debe contener 10 numeros ')
