from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reserva

from .serializers import ReservaSerializer, ClienteSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Reserva
from .forms import ReservaForm

from reservas.models import Reserva
from clientes.models import Cliente

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail

from django.template.loader import render_to_string
from weasyprint import HTML

from django.utils import timezone

def reporte_pdf(request):
    reservas = Reserva.objects.all().order_by('fecha_reserva')
    html_string = render_to_string('reservas/reporte_pdf.html', {'reservas': reservas})
    pdf = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reservas.pdf"'
    return response

def confirmar_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    send_mail(
        'Reserva Confirmada',
        f'Tu reserva para {reserva.nombre_cliente} está confirmada.',
        'tucorreo@gmail.com',
        [reserva.correo_cliente],
        fail_silently=False,
    )

@csrf_exempt
def disponibilidad_json(request):
    fecha = request.GET.get('fecha')
    disponibles = Mesa.objects.filter(reserva__fecha_reserva__ne=fecha)
    data = [{'id': m.id, 'numero': m.numero} for m in disponibles]
    return JsonResponse(data, safe=False)

def reservas_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reservas.pdf"'
    p = canvas.Canvas(response)
    y = 750
    for r in Reserva.objects.all():
        p.drawString(100, y, f"{r.id} - {r.fecha}")
        y -= 20
    p.showPage()
    p.save()
    return response

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

class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/reserva_form.html'
    success_url = reverse_lazy('reservas:list')
    
    def get_initial(self):
        return {'fecha_reserva': timezone.now().date()}

    def form_valid(self, form):
        mesa = form.cleaned_data['mesa']
        if mesa:
            mesa.ocupada = True
            mesa.save()
        return super().form_valid(form)

class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/reserva_form.html'
    success_url = reverse_lazy('reservas:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'fecha_reserva': self.object.fecha_reserva
        }
        return kwargs

class ReservaDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy('reservas:list')

    def delete(self, *args, **kwargs):
        reserva = self.get_object()
        if reserva.mesa:
            reserva.mesa.ocupada = False
            reserva.mesa.save()
        return super().delete(*args, **kwargs)