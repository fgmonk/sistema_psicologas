# sesiones/models.py
from django.db import models
from pacientes.models import Paciente

class Sesion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    observaciones = models.TextField(blank=True, null=True)

    ESTADOS = [
        ('programada', 'Programada'),
        ('realizada', 'Realizada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='programada')

    def __str__(self):
        return f"{self.paciente.nombre} - {self.fecha} {self.hora}"

