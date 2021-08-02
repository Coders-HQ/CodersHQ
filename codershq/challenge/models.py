from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _

from codershq.users.models import User


class Challenge(models.Model):

    VIRTUAL = 'VI'
    PHYSICAL = 'PH'
    HYBRID = 'HY'
    HACKATHON_TYPE = [
        (VIRTUAL, 'Virtual'),
        (PHYSICAL, 'Physical'),
        (HYBRID, 'Hybrid'),
    ]

    title = models.CharField(_("Title of Challenge"), max_length=100)
    subtitle = models.CharField(_("Little info to explain the Challenge."), max_length=150)
    slug = AutoSlugField(populate_from='title')
    challenge_type = models.CharField(_("Challenge Type"),
                                      max_length=2,
                                      choices=HACKATHON_TYPE,
                                      default=HACKATHON_TYPE[2])
    description = models.TextField(_("Challenge description"), max_length=5000,
                                   help_text="Describe the Challenge")
    evaluation = models.TextField(_("Challenge evaluation"), max_length=5000,
                                  help_text="Describe how will the challenge be evaluated")
    timeline = models.TextField(_("Challenge timeline"), max_length=5000,
                                help_text="Describe the Challenge's timeline")
    rules = models.TextField(_("Challenge rules"), max_length=5000,
                             help_text="Describe rules for the challenge")
    prizes = models.TextField(_("Challenge prize distrebution"), max_length=5000,
                              help_text="Describe how the prize money will be distributed")
    prize_money = models.PositiveIntegerField(_("Total prize money"), default=0)

    # dates
    join_date = models.DateField(_("Challenge join date"),
                                 help_text="When the competitors can start joining")
    date_start = models.DateField(_("Challenge start date"))
    date_end = models.DateField(_("Challenge end date"),
                                help_text="Challenge end date, no competitor can join after this date")
    last_join_date = models.DateField(_("Last join date"),
                                      help_text="Last date competitors can join")

    # users who have joined this challenge
    competitors = models.ManyToManyField(User)

    @property
    def prize_display(self):
        return f"{self.prize_money:,} AED"
