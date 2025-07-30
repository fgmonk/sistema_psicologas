from django.db import models
from pacientes.models import Paciente  # Ajusta según el nombre de tu app pacientes

class Sesion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente.rut} - {self.fecha} {self.hora}"
