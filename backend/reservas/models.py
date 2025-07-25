from django.db import models

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    capacidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=50)


class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    correo_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()
    estado = models.CharField(max_length=20,
        choices=[('pendiente', 'Pendiente'),
                ('confirmada', 'Confirmada'),
                ('cancelada', 'Cancelada')],
        default='pendiente')
    creado_en = models.DateTimeField(auto_now_add=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para el {self.fecha_reserva}"