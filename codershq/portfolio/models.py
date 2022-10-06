# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

"""
- About - large text
- *looking for job - bool
- *currently employed - bool
- Position (optional?)
- Employer (optional?)
- place of employment - text
- *Nationality - text..? this will be annoying. Drop down menu. We can find a standard list online
- *Country of Residence  - same
- *Mobile Number - number
- Github User Name
- LinkedIn Profile
"""


class Portfolio(models.Model):
    """
    Portfolio model
    """

    about = models.TextField(
        _("About"),
        blank=True,
        help_text=_("Tell us a bit about yourself"),
        max_length=1500)
    is_seeking_job = models.BooleanField(
        _("Seeking employment"),
        default=False,
        help_text=_("Are you looking for employment?"))
    is_working = models.BooleanField(
        _("Currently employed?"),
        default=False,
        help_text=_("Are you employed currently?"))
    employer = models.CharField(
        _("Your employer"),
        max_length=150,
        blank=True,
        null=True,
        help_text=_("(If currently employed)"))
    nationality = CountryField(
        blank_label='(select nationality)',
        blank=True
    )
    country_residence = CountryField(
        blank_label='(select country)',
        blank=True
    )
    mobile_number = models.CharField(
        _("Your mobile number"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("(eg: +97150XXXXXXX)"))
    github = models.CharField(
        _("Github account"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("https://github.com/Coders-HQ"))
    linkedin = models.CharField(
        _("Linkedin account"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("https://linkedin.com/in/XXXX")),

    # auto generated fields
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)