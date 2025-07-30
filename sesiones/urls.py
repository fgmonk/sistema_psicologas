from django.urls import path
from . import views

urlpatterns = [
    path('', views.sesiones_list, name='sesiones_list'),
    path('crear/', views.crear_sesion, name='crear_sesion'),
    path('editar_observacion/<int:pk>/', views.editar_observacion, name='editar_observacion'),
]
