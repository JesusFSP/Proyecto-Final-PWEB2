from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, time
from .models import Reserva, Mesa 

class ReservaForm(forms.ModelForm):
    fecha_reserva = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    hora_reserva = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {'mesa': forms.Select(attrs={'class': 'form-select'})}

    def __init__(self, *args, **kwargs):
        # Obtener la fecha que llega desde la vista
        fecha = kwargs.pop('initial', {}).get('fecha_reserva') or (self.instance and self.instance.fecha_reserva)
        super().__init__(*args, **kwargs)

        if fecha:
            ocupadas = (
                Reserva.objects
                .filter(fecha_reserva=fecha)
                .exclude(pk=self.instance.pk)
                .values_list('mesa', flat=True)
            )
            self.fields['mesa'].queryset = Mesa.objects.exclude(pk__in=ocupadas)
        else:
            # Fallback: todas las mesas libres
            self.fields['mesa'].queryset = Mesa.objects.filter(ocupada=False)

    def clean_fecha_reserva(self):
        fecha = self.cleaned_data['fecha_reserva']
        if fecha < timezone.now().date():
            raise ValidationError("La fecha debe ser futura.")
        return fecha

    def clean_hora_reserva(self):
        hora = self.cleaned_data['hora_reserva']
        return hora