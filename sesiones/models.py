from django.db import models
from pacientes.models import Paciente

class Sesion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    comentario = models.TextField(blank=True, null=True)

    MOTIVOS = [
    ('conductual', 'Conductual'),
    ('emocional', 'Emocional'),
    ('academico', 'Académico / Aprendizaje'),
    ('familiar', 'Familiar / Relaciones Familiares'),
    ('social', 'Social / Interacción con pares'),
    ('sueno', 'Trastornos del Sueño'),
    ('alimentacion', 'Trastornos de Alimentación'),
    ('desarrollo', 'Desarrollo / Habilidades'),
    ]
    motivo = models.CharField(max_length=20, choices=MOTIVOS)

    ESTADOS = [
        ('programada', 'Programada'),
        ('realizada', 'Realizada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='programada')

    def __str__(self):
        return f"{self.paciente.nombre} - {self.fecha} {self.hora}"
