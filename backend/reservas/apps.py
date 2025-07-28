from django.apps import AppConfig

class ReservasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservas'

    def ready(self):
        import reservas.signals
        from .models import Mesa
        if not Mesa.objects.exists():
            for i in range(1, 11):
                Mesa.objects.create(numero=i)