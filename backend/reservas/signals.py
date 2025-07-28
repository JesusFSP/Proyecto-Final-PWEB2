from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reserva

@receiver(post_save, sender=Reserva)
def mail_nueva_reserva(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Nueva reserva',
            f'Hola, tu reserva #{instance.pk} está confirmada para el {instance.fecha}.',
            'reservas@sazonperuana.com',
            [instance.email],
            fail_silently=False,
        )