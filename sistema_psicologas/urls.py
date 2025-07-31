from django.contrib import admin
from django.urls import path, include
from core.views import dashboard
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_required(dashboard), name='home'),

    # Login/logout (dentro de core)
    path('accounts/', include('core.urls')),

    # Solo pacientes habilitado
    path('pacientes/', include('pacientes.urls')),

    path('cobranza/', include('cobranza.urls')),
    path('sesiones/', include('sesiones.urls')),
    path('informes/', include('informes.urls')),

]
