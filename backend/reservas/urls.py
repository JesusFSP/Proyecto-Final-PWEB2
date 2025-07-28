from rest_framework.routers import DefaultRouter
from .views import ReservaViewSet, ClienteViewSet

router = DefaultRouter()
router.register(r'reservas', ReservaViewSet)
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),   # JSON
    path('', include('reservas.urls_web')),  # vistas HTML
]