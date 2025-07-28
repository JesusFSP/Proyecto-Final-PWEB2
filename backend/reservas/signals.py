from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reserva

@receiver(post_save, sender=Reserva)
def mail_nueva_reserva(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Nueva reserva',
            f'Reserva para {instance.nombre_cliente} el {instance.fecha_reserva} a las {instance.hora_reserva}',
            'tucorreo@gmail.com',
            [instance.correo_cliente],
            fail_silently=False,
        )