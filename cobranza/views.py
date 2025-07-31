from django.shortcuts import render
from .models import Cobranza

def listar_cobranzas(request):
    cobranzas = Cobranza.objects.select_related('sesion', 'sesion__paciente').all().order_by('-fecha_creacion')
    return render(request, 'cobranza/listar_cobranzas.html', {'cobranzas': cobranzas})
