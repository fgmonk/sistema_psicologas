from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cobranzas, name='listar_cobranzas'),
    path('marcar_pagada/<int:cobranza_id>/', views.marcar_pagada, name='marcar_pagada'),
    path('enviar_recordatorio/<int:cobranza_id>/', views.enviar_recordatorio, name='enviar_recordatorio'),
    path('editar_monto/<int:cobranza_id>/', views.editar_cobranza_inline, name='editar_cobranza_inline'),
]
