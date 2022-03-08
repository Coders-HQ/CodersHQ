from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils.eventbrite import Eventbrite

from codershq.users.models import User


def event_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/beat/author/<filename>
    event_title = instance.title.replace(" ", "_")
    new_filename = event_title + "." + filename.split(".")[1]
    return "event/image/{0}".format(new_filename)


class Event(models.Model):
    # event name
    title = models.CharField(_("Event title"), max_length=100)
    # event image to be displayed in card
    image = models.ImageField(_("Event image"), upload_to=event_image_path)
    # when the event starts
    date_time = models.DateTimeField(_("Event date and time"))
    # how long the event will last
    duration = models.IntegerField(_("Event duration (hrs)"), null=True, blank=True)
    # short event description
    short_description = models.CharField(
        _("Short event description"), max_length=140, default=None
    )
    # event description
    description = RichTextField()
    # event requirements
    requirements = RichTextField(
        _("Event requirements (like PCR, Vaccine, etc)"), blank=True, default=""
    )
    # event link
    event_link = models.URLField(
        _("Event zoom link (only if online)"), blank=True, null=True
    )
    event_location = models.CharField(
        _("Event location (use 'Online' if its online)"),
        max_length=150,
        blank=True,
        null=True,
    )
    seats = models.IntegerField(
        _("Number of seats available (if not online"), blank=True, null=True
    )

    # people who are intrested in the event
    attendees = models.ManyToManyField(User, related_name="attended_events", blank=True)
    # people who actually joined the event
    participants = models.ManyToManyField(
        User, related_name="participated_events", blank=True
    )

    def __str__(self):
        return self.title

    def is_over(self):
        return self.date_time < timezone.now()

    def location(self):
        if self.event_location is not None and self.event_location.lower() != "online":
            return "CHQ"
        return "Online"

    def get_time_left(self):
        if not self.is_over():
            time_now = timezone.now()
            end_date = self.date_time
            delta = end_date - time_now

            days_left = delta.days
            weeks_left = delta.days // 7
            months_left = delta.days // 30

            if days_left <= 7:
                return str(days_left) + " days"

            if weeks_left <= 4:
                return str(weeks_left) + " weeks"

            return str(months_left) + " months"

@receiver(post_save, sender=Event, dispatch_uid="create_eventbrite_event")
def create_eventbrite_event(sender, instance, **kwargs):
    Eventbrite(instance)