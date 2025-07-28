from django.shortcuts import render

def sesiones_list(request):
    return render(request, 'sesiones/lista.html')
