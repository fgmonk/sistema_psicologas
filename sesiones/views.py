from django.shortcuts import render, get_object_or_404, redirect
from .models import Sesion
from .forms import SesionForm, ObservacionForm  # Asegúrate de tener ambos formularios creados

def sesiones_list(request):
    sesiones = Sesion.objects.all().order_by('fecha', 'hora')
    return render(request, 'sesiones/sesiones_list.html', {'sesiones': sesiones})

def crear_sesion(request):
    if request.method == 'POST':
        form = SesionForm(request.POST)
        if form.is_valid():
            form.save()
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
