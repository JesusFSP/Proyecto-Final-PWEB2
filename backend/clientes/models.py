from django.db import models
from reservas.models import Reserva

class Cliente(models.Model):
    nombre   = models.CharField(max_length=100)
    email    = models.EmailField(unique=True)
    reservas = models.ManyToManyField(Reserva, related_name='clientes')

    def __str__(self):
        return self.nombre