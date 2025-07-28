from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    ocupada = models.BooleanField(default=False)

    def __str__(self):
        return f'Mesa {self.numero}'


class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    correo_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(20)
        ]
    )
    estado = models.CharField(max_length=20,
        choices=[('pendiente', 'Pendiente'),
                ('confirmada', 'Confirmada'),
                ('cancelada', 'Cancelada')],
        default='pendiente')
    creado_en = models.DateTimeField(auto_now_add=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para el {self.fecha_reserva}"