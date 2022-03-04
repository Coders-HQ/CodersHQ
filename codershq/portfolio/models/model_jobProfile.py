from django.db import models
from django.utils.translation import ugettext_lazy as _

from codershq.portfolio.models import Portfolio


class JobProfile(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    job_status = models.CharField(_("jobprofile_field_jobStatus"), max_length=50)
    hourly_rate = models.FloatField(_("jobprofile_field_hourlyRate"), default=5.0)
