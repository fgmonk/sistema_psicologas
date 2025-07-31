from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cobranzas, name='listar_cobranzas'),
]
