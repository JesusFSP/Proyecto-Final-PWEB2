
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def enviar_email_confirmacion(reserva):
    subject = 'Confirmación de Reserva - Sazón Peruana'
    html_message = render_to_string('reservas/email_confirmacion.html', {
        'reserva': reserva
    })
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        None,
        [reserva.correo_cliente],
        html_message=html_message
    )