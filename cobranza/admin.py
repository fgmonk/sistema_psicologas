from django.contrib import admin
from .models import Cobranza

@admin.register(Cobranza)
class CobranzaAdmin(admin.ModelAdmin):
    list_display = ('sesion', 'estado', 'monto', 'fecha_creacion', 'fecha_pago')
    list_filter = ('estado',)
    search_fields = ('sesion__paciente__nombre', 'sesion__paciente__rut')
