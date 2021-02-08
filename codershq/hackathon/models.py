from django.db import models
from django.utils.translation import gettext_lazy as _

class Hackathon(models.Model):
    description = models.TextField(_("Describe the Hackathon"),max_length=5000)
    evaluation = models.TextField(_("Describe how will the hackathon be evaluated"),max_length=5000)
    timeline = models.TextField(_("Describe the Hackathon's timeline"),max_length=5000)
    rules = models.TextField(_("Describe rules for the hackathon"),max_length=5000)
    prizes = models.TextField(_("Describe how the prize money will be distributed"),max_length=5000)
    prize_money = models.PositiveIntegerField(_("Total prize money"), default=0)

