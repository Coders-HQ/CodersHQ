from email.policy import default
from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .utils.eventbrite import Eventbrite

from codershq.users.models import User


def event_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/beat/author/<filename>
    event_title = instance.name.replace(" ", "_")
    new_filename = event_title + "." + filename.split(".")[1]
    return "event/image/{0}".format(new_filename)


class Event(models.Model):

    # 
    # Eventbrite main fields
    #

    # event name
    name = models.CharField(_("Event title"), max_length=100)
    # when the event starts
    start = models.DateTimeField(_("Event start date"))
    # when the event ends
    end = models.DateTimeField(_("Event end date time"))
    # short event description
    summary = models.CharField(
        _("Short event description"), max_length=140, default=None
    )
    # event description
    description = RichTextField()
    # if its online
    online_event = models.BooleanField(_("Is the event online?"), default=False)
    # number of seats available
    capacity = models.IntegerField(
        _("Number of seats available (if not online)"), blank=True, null=True
    )
    # show event if this is listed or else hide it
    listed = models.BooleanField(_("Show event in event list?"), default=True)
    # if true, displays the total number of remaining event tickets
    show_remaining = models.BooleanField(_("Show the total number of remaining event tickets"), default=False)

    # 
    # additional fields fields
    # 


    # event image to be displayed in card
    image = models.ImageField(_("Event image"), upload_to=event_image_path)
    # location of event
    event_location = models.CharField(
        _("Event location (use 'Online' if its online)"),
        max_length=150,
        blank=True,
        null=True,
    )
    # people who are intrested in the event
    attendees = models.ManyToManyField(User, related_name="attended_events", blank=True)
    # people who actually joined the event
    participants = models.ManyToManyField(
        User, related_name="participated_events", blank=True
    )

    # overwrites save method 
    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        print('should create an event')
        event = Eventbrite.create_event(self)

    def __str__(self):
        return self.name

    def is_over(self):
        return self.end < timezone.now()

    def location(self):
        if self.event_location is not None and self.event_location.lower() != "online":
            return "CHQ"
        return "Online"

    def get_time_left(self):
        if not self.is_over():
            time_now = timezone.now()
            end_date = self.start
            delta = end_date - time_now

            days_left = delta.days
            weeks_left = delta.days // 7
            months_left = delta.days // 30

            if days_left <= 7:
                return str(days_left) + " days"

            if weeks_left <= 4:
                return str(weeks_left) + " weeks"

            return str(months_left) + " months"