from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cobranza
from sesiones.models import Sesion
from datetime import date
from django.utils import timezone

# 1️⃣ Listar todas las cobranzas
@login_required
def listar_cobranzas(request):
    # Asegurar que todas las sesiones realizadas tengan una cobranza
    sesiones_realizadas = Sesion.objects.filter(estado='realizada')
    for sesion in sesiones_realizadas:
        Cobranza.objects.get_or_create(
            sesion=sesion,
            defaults={
                'fecha_creacion': timezone.now(),
                'estado': 'pendiente',
                'monto': 40000,  # monto base
            }
        )

    # Obtener todas las cobranzas ordenadas por fecha de sesión descendente
    cobranzas = (
        Cobranza.objects
        .select_related('sesion', 'sesion__paciente')
        .all()
        .order_by('-sesion__fecha', '-fecha_creacion')
    )

    return render(request, 'cobranza/listar_cobranzas.html', {'cobranzas': cobranzas})

# 2️⃣ Marcar una cobranza como pagada y enviar comprobante
@login_required
def marcar_pagada(request, cobranza_id):
    cobranza = get_object_or_404(Cobranza, pk=cobranza_id)
    if cobranza.estado != 'pagado':
        cobranza.estado = 'pagado'
        cobranza.fecha_pago = date.today()
        cobranza.save()

        # Enviar correo de comprobante de pago
        paciente_email = cobranza.sesion.paciente.correo_contacto
        subject = "Comprobante de pago"
        message = (
            f"Estimado/a {cobranza.sesion.paciente.nombre},\n\n"
            f"Se ha registrado el pago de la sesión del {cobranza.sesion.fecha}.\n"
            f"Monto: ${cobranza.monto}\n\nGracias.\nEquipo de psicología."
        )
        send_mail(subject, message, settings.EMAIL_HOST_USER, [paciente_email], fail_silently=False)

    return redirect('listar_cobranzas')

# 3️⃣ Enviar recordatorio de pago pendiente
@login_required
def enviar_recordatorio(request, cobranza_id):
    cobranza = get_object_or_404(Cobranza, pk=cobranza_id)
    if cobranza.estado != 'pagado':
        paciente_email = cobranza.sesion.paciente.correo_contacto
        subject = "Recordatorio de pago pendiente"
        message = (
            f"Estimado/a {cobranza.sesion.paciente.nombre},\n\n"
            f"Tiene un pago pendiente por la sesión del {cobranza.sesion.fecha}.\n"
            f"Monto: ${cobranza.monto}\n\nPor favor realice el pago a la brevedad.\n\nSaludos."
        )
        send_mail(subject, message, settings.EMAIL_HOST_USER, [paciente_email], fail_silently=False)
        messages.success(request, f"Recordatorio de pago enviado a {cobranza.sesion.paciente.nombre}")

    return redirect('listar_cobranzas')

# 4️⃣ Editar monto de una cobranza (inline)
@login_required
def editar_cobranza_inline(request, cobranza_id):
    cobranza = get_object_or_404(Cobranza, pk=cobranza_id)
    if request.method == 'POST':
        nuevo_monto = request.POST.get('monto')
        if nuevo_monto:
            try:
                cobranza.monto = float(nuevo_monto)
                cobranza.save()
                # Mensaje eliminado porque confirmación se hace en template
            except ValueError:
                pass  # Ignorar si no es un número válido
    return redirect('listar_cobranzas')
