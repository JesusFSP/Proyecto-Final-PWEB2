from rest_framework import generics
from .models import Reserva
from .serializers import ReservaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class DisponibilidadView(APIView):
    def get(self, request):
        fecha = request.query_params.get('fecha')
        hora = request.query_params.get('hora')
        personas = int(request.query_params.get('personas', 1))

        hora_reserva = timezone.datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
        hora_inicio = hora_reserva - timedelta(hours=2)
        hora_fin = hora_reserva + timedelta(hours=2)

        reservas_existentes = Reserva.objects.filter(
            fecha_reserva=fecha,
            hora_reserva__range=(hora_inicio.time(), hora_fin.time())
        ).count()

        disponible = reservas_existentes < 10

        return Response({'disponible': disponible, 'mesas_disponibles': 10 - reservas_existentes})