from django import forms
from django.core.exceptions import ValidationError
from .models import Reserva
import datetime

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
    
    def clean_fecha_reserva(self):
        fecha = self.cleaned_data['fecha_reserva']
        if fecha < datetime.date.today():
            raise forms.ValidationError("La fecha debe ser futura.")
        return fecha