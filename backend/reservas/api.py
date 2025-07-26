
from .models import Reserva, Mesa
from .serializers import ReservaSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from .utils import enviar_email_confirmacion

@api_view(['GET'])
def mesas_disponibles(request):
    fecha = request.GET.get('fecha')
    mesas = Mesa.objects.exclude(reserva__fecha_reserva=fecha)
    return Response({'mesas': [{'numero': m.numero, 'capacidad': m.capacidad} for m in mesas]})

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DisponibilidadView(APIView):
    def get(self, request):
        fecha = request.query_params.get('fecha')
        hora = request.query_params.get('hora')
        personas = int(request.query_params.get('personas', 1))

        try:
            hora_reserva = datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
        except ValueError:
            return Response({'error': 'Formato de fecha/hora inválido'}, status=400)

        mesas_disponibles = Mesa.objects.filter(
            capacidad__gte=personas
        ).exclude(
            reserva__fecha_reserva=fecha,
            reserva__hora_reserva__range=(
                (hora_reserva - timedelta(hours=2)).time(),
                (hora_reserva + timedelta(hours=2)).time()
            )
        )

        return Response({
            'disponible': mesas_disponibles.exists(),
            'mesas': MesaSerializer(mesas_disponibles, many=True).data
        })