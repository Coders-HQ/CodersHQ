from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Challenge(models.Model):
    """Main challenge model"""

    # the name of the challenge
    name = models.CharField(_("Name of Challenge"), max_length=100)

    short_description = models.TextField(
        _("Short challenge description"), max_length=20, help_text="Short description of the challenge"
    )
    description = RichTextField()
    image = models.ImageField(_("Challenge Image"), upload_to="challenges/image/", blank=True, default=None, null=None)
    github_link = models.URLField(_("Challenge github link"),  default=None, blank=True, null=True)
    website = models.URLField(_("Website link"), null=True, blank=True)
    train_data = models.URLField(_("Train data link"), null=True, blank=True, help_text="Link to train data set")
    test_data = models.URLField(_("Test data link"), null=True, blank=True, help_text="Link to test data set")

    def __str__(self) -> str:
        return "Challenge: " + self.name
