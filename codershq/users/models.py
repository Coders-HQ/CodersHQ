from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    """Default user for Coders Headquarters."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    bio = models.TextField(_("Biography"), blank=True, max_length=500)
    cv = models.FileField(_("User's CV"), null=True, blank=True, upload_to="cv")
    academic_qualification = models.CharField(_("User's highest qualification"), blank=True, max_length=30)
    academic_qualification_file = models.FileField(null=True, blank=True, upload_to="academic")
    github_profile = models.CharField(_("User's GitHub profile"),blank=True, max_length=255)
    github_score = models.IntegerField(null=False, default=0)
    front_end_score = models.IntegerField(null=False, default=20)
    back_end_score = models.IntegerField(null=False, default=20)
    database_score = models.IntegerField(null=False, default=20)
    devops_score = models.IntegerField(null=False, default=20)
    mobile_score = models.IntegerField(null=False, default=20)
    
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
