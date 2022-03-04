from django.db import models
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models.model_portfolio import Portfolio

PROFICIENCY_LEVELS = (
    (1, 'Beginner'),
    (2, 'Intermediate'),
    (3, 'Advanced')
)


class Language(models.Model):
    user_profile = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    name = models.CharField(_("language_field_name"), max_length=50)
    proficiency = models.SmallIntegerField(_("language_field_proficiency"), choices=PROFICIENCY_LEVELS)

