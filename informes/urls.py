# informes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_informes, name='listar_informes'),
    path('crear/', views.crear_informe, name='crear_informe'),
    path('editar/<int:pk>/', views.editar_informe, name='editar_informe'),
    path('<int:pk>/', views.detalle_informe, name='detalle_informe'),
    path('exportar_pdf/<int:pk>/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar_word/<int:pk>/', views.exportar_word, name='exportar_word'),
]
