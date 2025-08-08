from django.shortcuts import render, get_object_or_404, redirect
from .models import Sesion
from .forms import SesionForm, ObservacionForm  
from django.core.mail import send_mail
from django.conf import settings

def sesiones_list(request):
    sesiones = Sesion.objects.all().order_by('fecha', 'hora')
    return render(request, 'sesiones/sesiones_list.html', {'sesiones': sesiones})

def crear_sesion(request):
    if request.method == 'POST':
        form = SesionForm(request.POST)
        if form.is_valid():
            sesion = form.save()

            # Preparar datos para el correo
            paciente_email = sesion.paciente.correo_contacto
            fecha = sesion.fecha.strftime('%d-%m-%Y')
            hora = sesion.hora.strftime('%H:%M')
            subject = 'Confirmación de sesión agendada'
            message = f'Estimado/a,\n\nSe ha agendado una sesión para el día {fecha} a las {hora}.\n\nSaludos,\nEquipo de psicología.'

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # correo configurado en settings.py
                [paciente_email],
                fail_silently=False,
            )

            return redirect('sesiones_list')
    else:
        form = SesionForm()
    return render(request, 'sesiones/crear_sesion.html', {'form': form})

def editar_observacion(request, pk):
    sesion = get_object_or_404(Sesion, pk=pk)
    if request.method == 'POST':
        form = ObservacionForm(request.POST, instance=sesion)
        if form.is_valid():
            form.save()
            return redirect('sesiones_list')
    else:
        form = ObservacionForm(instance=sesion)
    return render(request, 'sesiones/editar_observacion.html', {'form': form, 'sesion': sesion})
