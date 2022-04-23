from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .utils.eventbrite import Eventbrite
from .models import Event


@receiver(pre_save, sender=Event)
def save_event(sender, instance, *args, **kwargs):
    event_id = Eventbrite.create_event(instance)
    instance.eventbrite_id = event_id


@receiver(pre_delete, sender=Event)
def delete_event(sender, instance, *args, **kwargs):
    response = Eventbrite.delete_event(instance, instance.eventbrite_id)
