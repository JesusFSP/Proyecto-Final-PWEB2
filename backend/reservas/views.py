from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reserva, Cliente
from .serializers import ReservaSerializer, ClienteSerializer

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Reserva
from .forms import ReservaForm

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ReservaListView(ListView):
    model               = Reserva
    template_name       = 'reservas/reserva_list.html'
    context_object_name = 'reservas'

class ReservaDetailView(DetailView):
    model               = Reserva
    template_name       = 'reservas/reserva_detail.html'
    context_object_name = 'reserva'

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model         = Reserva
    form_class    = ReservaForm
    template_name = 'reservas/reserva_form.html'
    success_url   = reverse_lazy('reservas:list')

class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model         = Reserva
    form_class    = ReservaForm
    template_name = 'reservas/reserva_form.html'
    success_url   = reverse_lazy('reservas:list')

class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model         = Reserva
    template_name = 'reservas/reserva_confirm_delete.html'
    success_url   = reverse_lazy('reservas:list')