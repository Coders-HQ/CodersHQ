from django.db import models
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Portfolio


class Education(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(_("education_field_name"), max_length=50, null=False, blank=False)
    education_level = models.CharField(_("education_field_educationLevel"), max_length=50, null=True, blank=True)
    end_date = models.DateField(_("education_field_endDate"))
