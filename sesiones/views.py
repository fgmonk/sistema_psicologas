# sesiones/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import messages
from django.conf import settings
from datetime import time

from .models import Sesion
from .forms import SesionForm, ObservacionForm
from cobranza.models import Cobranza

# -----------------------------
# LISTADO DE SESIONES
# -----------------------------
@login_required
def sesiones_list(request):
    sesiones = Sesion.objects.all().order_by('-fecha', '-hora')
    return render(request, 'sesiones/sesiones_list.html', {'sesiones': sesiones})

# -----------------------------
# CREAR NUEVA SESIÓN
# -----------------------------
@login_required
def crear_sesion(request):
    if request.method == 'POST':
        form = SesionForm(request.POST)
        if form.is_valid():
            sesion = form.save(commit=False)
            
            # Validar hora
            if not (time(8, 0) <= sesion.hora <= time(18, 0)):
                messages.error(request, "La hora debe estar entre 08:00 y 18:00.")
                return render(request, 'sesiones/crear_sesion.html', {'form': form})
            # Validar día hábil
            if sesion.fecha.weekday() >= 5:
                messages.error(request, "No se pueden agendar sesiones en fines de semana.")
                return render(request, 'sesiones/crear_sesion.html', {'form': form})

            sesion.save()

            # Enviar correo
            paciente_email = sesion.paciente.correo_contacto
            fecha = sesion.fecha.strftime('%d-%m-%Y')
            hora = sesion.hora.strftime('%H:%M')
            subject = 'Confirmación de sesión agendada'
            message = f'Estimado/a,\n\nSe ha agendado una sesión para el día {fecha} a las {hora}.\n\nSaludos,\nEquipo de psicología.'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [paciente_email], fail_silently=False)

            messages.success(request, "Sesión creada correctamente.")
            return redirect('sesiones_list')
    else:
        form = SesionForm()
    return render(request, 'sesiones/crear_sesion.html', {'form': form})

# -----------------------------
# EDITAR COMENTARIO DE SESIÓN
# -----------------------------
@login_required
def editar_observacion(request, pk):
    sesion = get_object_or_404(Sesion, pk=pk)
    if request.method == 'POST':
        form = ObservacionForm(request.POST, instance=sesion)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentario actualizado correctamente.")
            return redirect('sesiones_list')
    else:
        form = ObservacionForm(instance=sesion)
    return render(request, 'sesiones/editar_observacion.html', {'form': form, 'sesion': sesion})

# -----------------------------
# MARCAR SESIÓN COMO REALIZADA
# -----------------------------
@login_required
def marcar_realizada(request, pk):
    sesion = get_object_or_404(Sesion, pk=pk)
    
    if sesion.estado == 'programada':
        sesion.estado = 'realizada'
        sesion.save()

        # Crear registro en Cobranza si no existe
        Cobranza.objects.get_or_create(
            sesion=sesion,
            defaults={
                'fecha_creacion': timezone.now(),
                'estado': 'pendiente',
                'monto': 0,
            }
        )

    return redirect('sesiones_list')
