"""
URL configuration for sazon_peruana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reservas import views
from rest_framework import routers
from reservas.api import ReservaViewSet 
from reservas.api import DisponibilidadView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/nueva/', views.crear_reserva, name='crear_reserva'),
    path('api/', include(router.urls)),
    path('api/disponibilidad/', DisponibilidadView.as_view(), name='disponibilidad'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
