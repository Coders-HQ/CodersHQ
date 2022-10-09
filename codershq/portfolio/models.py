# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.validators import URLValidator
from django.core.validators import MaxValueValidator, MinValueValidator


def user_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/beat/author/<filename>
    return "profile/image/{0}".format( filename)


class Portfolio(models.Model):
    """
    Portfolio model
    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        
    )
    EMPLOYMENT_TIME_CHOICES = (
        ('F', 'Fulltime'),
        ('P', 'Part-Time'),
    )

    first_name = models.CharField(_("First Name"), blank=False, max_length=255)
    last_name = models.CharField(_("Last Name"), blank=False, max_length=255)
    gender = models.CharField(
        _("Gender"),
        null=True,
        blank=False,
        max_length=1,
        choices=GENDER_CHOICES,
    )
    nationality = CountryField(
        blank_label='(select nationality)',
        blank=False,
    )
    country_residence = CountryField(
        blank_label='(select country)',
        blank=False,
    )
    mobile_number = models.CharField(
        _("Your mobile number"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("(eg: +97150XXXXXXX)"))
    about = models.TextField(
        _("About"),
        blank=True,
        help_text=_("Tell us a bit about yourself"),
        max_length=1500)
    is_seeking_job = models.BooleanField(
        _("Seeking employment?"),
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

    github = models.CharField(
        _("Github account"),
        max_length=100,
        blank=True,
        validators=[URLValidator],
        null=True,
        help_text=_("https://github.com/Coders-HQ"))
    linkedin = models.CharField(
        _("Linkedin account"),
        max_length=100,
        validators=[URLValidator],
        blank=True,
        null=True,
        help_text=_("https://linkedin.com/in/XXXX"))
    twitter = models.CharField(
        _("Twitter account"),
        max_length=100,
        validators=[URLValidator],
        blank=True,
        null=True,
        help_text=_("https://twitter.com/coders_hq"))

    fav_language = models.CharField(
        _("Whats your favourite language?"),
        help_text=_("This can be a language or framework"),
        null=True,
        blank=True,
        max_length=50)
    employment_time = models.CharField(
        _("Do you like to work full-time or part-time?"),
        null=True,
        blank=True,
        max_length=1,
        choices=EMPLOYMENT_TIME_CHOICES,
    )
    personal_site = models.URLField(
        _("Do you have a personal site?"),
        null=True,
        validators=[URLValidator],
        blank=True,
    )
    proud_project = models.TextField(
        _("Tell us about the project that you are most proud of"),
        blank=True,
        help_text=_("This can be any project that you were involved in"),
        max_length=2500)
    academic_qualification = models.CharField(
        _("Your highest academic qualification"), blank=True, max_length=30
    )
    profile_image = models.ImageField(
        _("Profile image"), upload_to=user_image_path, null=True, blank=True
    )
    years_experience = models.IntegerField(
        _("Years of experience"),
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    # auto generated fields
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
