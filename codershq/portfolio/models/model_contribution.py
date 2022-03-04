from django.db import models
from django.utils.translation import ugettext_lazy as _

from codershq.portfolio.models import Portfolio, Task


class Contribution(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    contributor_role = models.CharField(_("contribution_field_role"), max_length=50)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
