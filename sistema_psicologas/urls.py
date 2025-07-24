from django.contrib import admin
from django.urls import path, include
from core.views import dashboard
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),

    # Menú principal, protegido por login
    path('', login_required(dashboard), name='home'),

    # Login y logout en /accounts/
    path('accounts/', include('core.urls')),

    path('pacientes/', include('pacientes.urls')),
    path('sesiones/', include('sesiones.urls')),
    path('informes/', include('informes.urls')),
    path('pagos/', include('pagos.urls')),
]
