from django.db import models

class Paciente(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    centro_educacional = models.CharField(max_length=100)
    nombre_apoderado = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    correo_contacto = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.rut})"