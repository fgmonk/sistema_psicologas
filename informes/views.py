# informes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Informe
from .forms import InformeForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_informes(request):
    informes = Informe.objects.all().order_by('-fecha')
    return render(request, 'informes/listar_informes.html', {'informes': informes})

@login_required
def crear_informe(request):
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_informes')
    else:
        form = InformeForm()
    return render(request, 'informes/crear_informe.html', {'form': form})

@login_required
def editar_informe(request, informe_id):
    informe = get_object_or_404(Informe, pk=informe_id)
    if request.method == 'POST':
        form = InformeForm(request.POST, instance=informe)
        if form.is_valid():
            form.save()
            return redirect('listar_informes')
    else:
        form = InformeForm(instance=informe)
    return render(request, 'informes/editar_informe.html', {'form': form, 'informe': informe})
