from django.shortcuts import render

def lista_informes(request):
    return render(request, 'informes/lista.html')
