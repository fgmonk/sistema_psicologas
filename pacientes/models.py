from django.db import models
from django.core.exceptions import ValidationError
import re


def validar_rut(value):
    """
    Valida RUT chileno con dígito verificador.
    Formato esperado: 12.345.678-9 o 12345678-9
    """
    # Limpiar puntos y pasar a mayúscula
    rut = value.replace(".", "").upper()
    # Separar número y dígito verificador
    if "-" not in rut:
        raise ValidationError("Formato inválido. Ejemplo: 12.345.678-9")
    
    numero, dv = rut.split("-")
    
    if not numero.isdigit():
        raise ValidationError("El RUT debe contener solo números antes del guion.")




class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    # Dirección dividida en campos
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    # Centro educacional restringido a opciones
    CENTROS = [
        ("Arrayán", "Colegio Arrayán"),
        ("Niños Felices", "Colegio Niños Felices"),
    ]
    centro_educacional = models.CharField(max_length=50, choices=CENTROS)

    # Datos del apoderado
    nombre_apoderado = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    correo_contacto = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.rut})"
