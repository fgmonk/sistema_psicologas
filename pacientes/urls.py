from django.urls import path
from . import views

urlpatterns = [
    path('', views.paciente_list, name='paciente_list'),
    path('nuevo/', views.paciente_create, name='paciente_create'),
    path('<int:pk>/editar/', views.paciente_edit, name='paciente_edit'),
]
