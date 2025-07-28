from django.urls import path
from . import views

urlpatterns = [
    path('', views.sesiones_list, name='sesiones_list'),
]
