from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from codershq.users.models import User


def event_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/beat/author/<filename>
    return 'event/image/{0}'.format(filename)


class Event(models.Model):
    title = models.CharField(_("Event title"), max_length=100)
    image = models.ImageField(_("Event image"), upload_to=event_image_path)
    date_time = models.DateTimeField(_("Event date and time"))
    duration = models.IntegerField(_("Event duration (hrs)"), null=True, blank=True)
    description = RichTextField()
    short_description = models.CharField(_("Short event description"), max_length=500, default=None)
    event_link = models.URLField(_("Event zoom link (only if online)"), blank=True, null=True)
    event_location = models.CharField(_("Event location (use 'Online' if its online)"),
                                      max_length=150, blank=True, null=True)
    seats = models.IntegerField(_("Number of seats available (if not online"), blank=True, null=True)

    # people who are intrested in the event
    attendees = models.ManyToManyField(User, related_name='attended_events', blank=True)
    # people who actually joined the event
    participants = models.ManyToManyField(User, related_name='participated_events', blank=True)

    def __str__(self):
        return self.title

    def is_over(self):
        return self.date_time < timezone.now()
