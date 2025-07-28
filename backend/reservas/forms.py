from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model  = Reserva
        fields = '__all__'

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < date.today():
            raise ValidationError("La fecha no puede ser pasada.")
        return fecha