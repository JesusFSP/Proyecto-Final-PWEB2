from django.apps import AppConfig


class ReservasConfig(AppConfig):
    name = 'reservas'
    def ready(self):
        import reservas.signals
