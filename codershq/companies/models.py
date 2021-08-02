from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from codershq.challenge.models import Sprint


class Company(models.Model):
    """Main company model"""
    name = models.CharField(_("Comany name"), max_length=100)
    # logo size https://www.logaster.com/blog/logo-sizes/#company2
    logo = models.ImageField(_("Company logo"), upload_to='logo/',
                             max_length=100)
    website = models.URLField(_("Company website"), max_length=200)
    # to track the user who created the company
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('companies:company-list')


class SponsorshipTypes(models.Model):
    """Company sponsor types"""

    sponsorship_type = models.CharField(_("Company sponsorship type"), max_length=100)
    sponsorship_description = models.CharField(_("Company sponsorship description"), max_length=250)


class Sponsorships(models.Model):
    """Company sponsorship detail and value"""
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
    )
    sponsorship_type = models.OneToOneField(
        SponsorshipTypes,
        on_delete=models.CASCADE,
    )
    sprint = models.ForeignKey(
        Sprint,
        on_delete=models.CASCADE,
    )
    sponsorship_value = models.PositiveIntegerField(
        _("Sponsorship Value"),
        default=0,
        validators=[MaxValueValidator(10000000)]
    )
