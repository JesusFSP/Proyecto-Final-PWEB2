from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaViewSet, ClienteViewSet
from .views import (
    ReservaListView,
    ReservaDetailView,
    ReservaCreateView,
    ReservaUpdateView,
    ReservaDeleteView,
)

app_name = 'reservas'

router = DefaultRouter()
router.register(r'reservas', ReservaViewSet)
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('',           ReservaListView.as_view(),    name='list'),
    path('<int:pk>/',  ReservaDetailView.as_view(),  name='detail'),
    path('nueva/',     ReservaCreateView.as_view(),  name='create'),
    path('<int:pk>/editar/', ReservaUpdateView.as_view(), name='update'),
    path('<int:pk>/borrar/', ReservaDeleteView.as_view(), name='delete'),
]