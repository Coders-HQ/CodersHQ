from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Portfolio


class Ambassador(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    student_email = models.EmailField(_("ambassador_field_studentEmail"))
    student_phone = models.IntegerField(_("ambassador_field_studentPhone"))
    university_name = models.CharField(_("ambassador_field_university"), max_length=60)
    responsibilities = models.CharField(_("ambassador_field_responsibilities"), max_length=60)
    start_date = models.DateField(_("ambassador_field_startDate"), default=timezone.now)
    end_date = models.DateField(_("ambassador_field_endDate"), default=timezone.now)
