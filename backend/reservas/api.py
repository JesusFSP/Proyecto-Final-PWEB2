from rest_framework import generics
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer