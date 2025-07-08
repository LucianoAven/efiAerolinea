
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from aerolinea.models import Reserva

# Cambia el estado del asiento a "ocupado" cuando se crea una reserva
@receiver(post_save, sender=Reserva)
def actualizar_estado_asiento_reservado(sender, instance, created, **kwargs):
    if created:
        asiento = instance.asiento_id
        asiento.estado = 'ocupado'
        asiento.save()

# Cambia el estado del asiento a "disponible" cuando se elimina una reserva
@receiver(post_delete, sender=Reserva)
def actualizar_estado_asiento_disponible(sender, instance, **kwargs):
    asiento = instance.asiento_id
    asiento.estado = 'disponible'
    asiento.save()

