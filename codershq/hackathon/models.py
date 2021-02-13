from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from codershq.users.models import User


class Hackathon(models.Model):

    VIRTUAL = 'VI'
    PHYSICAL = 'PH'
    HYBRID = 'HY'
    HACKATHON_TYPE = [
        (VIRTUAL, 'Virtual'),
        (PHYSICAL, 'Physical'),
        (HYBRID, 'Hybrid'),
    ]

    title = models.CharField(_("Title of Hackathon"), max_length=100)
    slug = AutoSlugField(populate_from='title')
    hackathon_type = models.CharField(_("Hackathon Type"),
                                      max_length=2,
                                      choices=HACKATHON_TYPE,
                                      default=HACKATHON_TYPE[2])
    description = models.TextField(_("Hackathon description"), max_length=5000,
                                   help_text="Describe the Hackathon")
    evaluation = models.TextField(_("Hackathon evaluation"), max_length=5000,
                                  help_text="Describe how will the hackathon be evaluated")
    timeline = models.TextField(_("Hackathon timeline"), max_length=5000,
                                help_text="Describe the Hackathon's timeline")
    rules = models.TextField(_("Hackathon rules"), max_length=5000,
                             help_text="Describe rules for the hackathon")
    prizes = models.TextField(_("Hackathon prize distrebution"), max_length=5000,
                              help_text="Describe how the prize money will be distributed")
    prize_money = models.PositiveIntegerField(_("Total prize money"), default=0)
    join_date = models.DateField(_("Hackathon join date"),
                                 help_text="When the competitors can start joining")
    date_start = models.DateField(_("Hackathon start date"))
    date_end = models.DateField(_("Hackathon end date"),
                                help_text="Hackathon end date, no competitor can join after this date")
    last_join_date = models.DateField(_("Last join date"),
                                      help_text="Last date competitors can join")
    competitors = models.ManyToManyField(User)

    @property
    def prize_display(self):
        return f"{self.prize_money:,} AED"

    
