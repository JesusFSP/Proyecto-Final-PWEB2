from django.core.exceptions import ValidationError
import datetime as dt

class ReservaForm(forms.ModelForm):
    class Meta:
        model  = Reserva
        fields = '__all__'

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < dt.date.today():
            raise ValidationError("La fecha no puede ser pasada.")
        return fecha