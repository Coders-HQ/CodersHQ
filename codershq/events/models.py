from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from ckeditor.fields import RichTextField

def event_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/beat/author/<filename>
    return 'event/image/{0}'.format( filename)

class Event(models.Model):
    title = models.CharField(_("Event title"), max_length=100)
    image = models.ImageField(_("Event image"), upload_to=event_image_path)
    date_time = models.DateTimeField(_("Event date and time"))
    duration = models.IntegerField(_("Event duration (hrs)"), null=True, blank=True)
    short_description = models.CharField(_("Short event description"), max_length=500)
    description = RichTextField()
    event_link = models.URLField(_("Event zoom link (only if online)"), blank=True, null=True)
    event_location = models.CharField(_("Event location (use 'Online' if its online)"), max_length=150, blank=True, null=True)
    seats = models.IntegerField(_("Number of seats available (if not online"), blank=True, null=True)

    def __str__(self):
        return self.title

    def is_over(self):
        return self.date_time < datetime.today().date()