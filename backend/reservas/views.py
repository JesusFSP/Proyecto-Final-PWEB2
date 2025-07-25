from django.shortcuts import render
from .models import Reserva

def home(request):
    return render(request, 'reservas/home.html')

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    return render(request, 'reservas/crear_reserva.html')