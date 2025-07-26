from django.shortcuts import render
from .models import Reserva
from django.core.mail import send_mail
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReservaSerializer


def home(request):
    return render(request, 'reservas/home.html')


def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})


def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()

            send_mail(
                'Confirmación de Reserva - Sazón Peruana',
                f'Detalles de tu reserva:\n\nNombre: {reserva.nombre_cliente}\nFecha: {reserva.fecha_reserva}\nHora: {reserva.hora_reserva}',
                'reservas@sazonperuana.com',
                [reserva.correo_cliente],
                fail_silently=False,
            )

            return redirect('home')
    else:
        form = ReservaForm()

    return render(request, 'reservas/crear_reserva.html', {'form': form})
