from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, time
from .models import Reserva

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

    def clean_fecha_reserva(self):
        fecha = self.cleaned_data['fecha_reserva']
        if fecha < timezone.now().date():
            raise ValidationError("La fecha debe ser futura.")
        return fecha

    def clean_hora_reserva(self):
        hora = self.cleaned_data['hora_reserva']        
        return hora