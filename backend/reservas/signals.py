# reservas/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Reserva

@receiver(post_save, sender=Reserva)
def mail_reserva(sender, instance, created, **kwargs):
    if created:
        asunto = 'Nueva reserva creada – Sazón Peruana'
        mensaje = (
            f'Hola {instance.nombre_cliente},\n\n'
            f'Tu reserva ha sido CONFIRMADA:\n'
            f'• Fecha: {instance.fecha_reserva}\n'
            f'• Hora: {instance.hora_reserva}\n'
            f'• Personas: {instance.cantidad_personas}\n'
            f'• Mesa: {instance.mesa.numero if instance.mesa else "Sin asignar"}\n\n'
            f'¡Te esperamos!'
        )
    else:
        asunto = 'Reserva actualizada – Sazón Peruana'
        mensaje = (
            f'Hola {instance.nombre_cliente},\n\n'
            f'Tu reserva ha sido MODIFICADA:\n'
            f'• Fecha: {instance.fecha_reserva}\n'
            f'• Hora: {instance.hora_reserva}\n'
            f'• Personas: {instance.cantidad_personas}\n'
            f'• Mesa: {instance.mesa.numero if instance.mesa else "Sin asignar"}\n\n'
            f'Gracias por mantenerte al día.'
        )

    send_mail(
        asunto,
        mensaje,
        settings.DEFAULT_FROM_EMAIL,
        [instance.correo_cliente],
        fail_silently=False,
    )