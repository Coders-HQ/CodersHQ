from autoslug import AutoSlugField
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.translation import gettext_lazy as _

from codershq.users.models import User


class Challenge(models.Model):
    """Main challenge model"""

    name = models.CharField(_("Name of Challenge"), max_length=100)
    description = models.TextField(_("Challenge description"), max_length=5000,
                                   help_text="Describe the Challenge")
    logo = models.ImageField(_("Challenge Logo"), upload_to='challenges/logo/')
    github_link = models.TextField(_("Challenge github link"), default=None)
    website = models.TextField(_("Website link"), max_length=100)
    slack_group = models.TextField(_("Slack group"), default=None, max_length=100)
    cloud_provider = models.TextField(_("Cloud Provider"), default=None, max_length=100)
    cloud_provider_url = models.URLField(_("Cloud Provider URL"), default=None)
    cloud_provider_token = models.TextField(_("Cloud Provider token"), default=None, max_length=500)


class Sprint(models.Model):
    """Every challenge should have at least one sprint"""

    start_date = models.DateField(_("Sprint start date"))
    end_date = models.DateField(_("Sprint end date"))
    title = models.TextField(_("Sprint title"), max_length=100)
    description = models.TextField(_("Sprint Description"), max_length=5000)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class ScoreCategory(models.Model):
    """Category of challenge scoring"""
    description = models.TextField(_("Category of challenge scoring"), max_length=100)


class Score(models.Model):
    score_category = models.OneToOneField(ScoreCategory, on_delete=models.CASCADE)
    sprints = models.OneToOneField(Sprint, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(_("Sprint score"))
