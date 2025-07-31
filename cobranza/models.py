from django.db import models
from sesiones.models import Sesion

class Cobranza(models.Model):
    sesion = models.OneToOneField(Sesion, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')],
        default='pendiente'
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_pago = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.sesion.paciente.rut} - {self.sesion.fecha} - {self.estado}"
