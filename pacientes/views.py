from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente
from sesiones.models import Sesion
from informes.models import Informe
from .forms import PacienteForm
from django.contrib.auth.decorators import login_required

@login_required
def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

@login_required
def paciente_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    # Filtrar sesiones e informes asociados al paciente
    sesiones = Sesion.objects.filter(paciente=paciente)
    sesiones_programadas = sesiones.filter(estado='programada')  # Ajusta si usas otro campo
    sesiones_realizadas = sesiones.filter(estado='realizada')    # Ajusta si usas otro campo

    informes = Informe.objects.filter(paciente=paciente)

    context = {
        'paciente': paciente,
        'sesiones_programadas': sesiones_programadas,
        'sesiones_realizadas': sesiones_realizadas,
        'informes': informes,
    }

    return render(request, 'pacientes/paciente_detail.html', context)

@login_required
def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/formulario.html', {'form': form})

@login_required
def paciente_edit(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/formulario.html', {'form': form})
