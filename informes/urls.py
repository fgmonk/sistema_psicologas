from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_informes, name='informes_list'),  # esta es la URL que falta
]
