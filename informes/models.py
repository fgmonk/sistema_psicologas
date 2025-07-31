# informes/models.py
from django.db import models
from pacientes.models import Paciente

TIPOS_INFORME = (
    ('1', 'Informe tipo 1 - Colegio'),
    ('2', 'Informe tipo 2 - Familia'),
    ('3', 'Informe en blanco'),
)

class Informe(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPOS_INFORME)
    fecha = models.DateField(auto_now_add=True)
    contenido = models.TextField(blank=True)

    def __str__(self):
        return f"Informe {self.get_tipo_display()} - {self.paciente.nombre} ({self.fecha})"
