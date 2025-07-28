
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.ReservaListView.as_view(), name='lista'),
    path('<int:pk>/', views.ReservaDetailView.as_view(), name='detalle'),
    path('crear/', views.ReservaCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', views.ReservaUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.ReservaDeleteView.as_view(), name='eliminar'),
    path('api/disponibilidad/', views.disponibilidad_json, name='api_disponibilidad'),
]