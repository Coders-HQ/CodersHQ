from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Portfolio


class Task(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    t_name = models.CharField(_("task_field_name"), max_length=100)
    t_description = models.CharField(_("task_field_description"), max_length=300)
    t_difficulty = models.CharField(_("task_field_difficulty"), max_length=50)
    end_date = models.DateField(_("task_field_endDate"), default=timezone.now)

    def __str__(self):
        return "{name}".format(name=self.t_name)
