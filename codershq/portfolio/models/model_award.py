from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Portfolio


class Award(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(_('award_field_awardName'), max_length=50, null=False, blank=False)
    date_awarded = models.DateField('award_field_awardDate', null=False, blank=False, default=timezone.now)
