
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.ReservaListView.as_view(), name='list'),
    path('<int:pk>/', views.ReservaDetailView.as_view(), name='detail'),
    path('crear/', views.ReservaCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.ReservaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ReservaDeleteView.as_view(), name='delete'),
    path('api/disponibilidad/', views.disponibilidad_json, name='api_disponibilidad'),
    path('reporte/pdf/', views.reporte_pdf, name='reporte_pdf'),
]