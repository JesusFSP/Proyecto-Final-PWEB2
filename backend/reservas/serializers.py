from .models import Reserva
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    clientes = ClienteSerializer(many=True, read_only=True)
    class Meta:
        model = Reserva
        fields = '__all__'
        extra_kwargs = {
            'fecha_reserva': {
                'input_formats': ['%Y-%m-%d'],
                'error_messages': {
                    'invalid': 'Formato de fecha inválido. Use YYYY-MM-DD.'
                }
            },
            'hora_reserva': {
                'input_formats': ['%H:%M:%S'],
                'error_messages': {
                    'invalid': 'Formato de hora inválido. Use HH:MM:SS.'
                }
            }
        }

    def validate(self, data):
        # Validación combinada de fecha y hora
        try:
            fecha = data.get('fecha_reserva')
            hora = data.get('hora_reserva')

            if fecha and hora:
                reserva_datetime = timezone.make_aware(
                    datetime.combine(fecha, hora))

                if reserva_datetime < timezone.now():
                    raise serializers.ValidationError(
                        "La reserva debe ser en el futuro")
        except Exception as e:
            raise serializers.ValidationError(str(e))

        return data
