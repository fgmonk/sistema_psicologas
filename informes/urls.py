# informes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_informes, name='listar_informes'),
    path('crear/', views.crear_informe, name='crear_informe'),
    path('editar/<int:informe_id>/', views.editar_informe, name='editar_informe'),
]
