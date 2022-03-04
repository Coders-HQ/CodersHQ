from django.db import models
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import JobProfile


class Service(models.Model):
    job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
    name = models.CharField(
        _("service_field_name"), max_length=50, null=True, blank=True
    )
