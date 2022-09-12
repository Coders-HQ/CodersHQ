from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from codershq.users.validators import validate_github_profile


def user_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/beat/author/<filename>
    return "profile/image/{0}/{1}".format(instance.username, filename)


class User(AbstractUser):
    """Default user for Coders Headquarters."""

    # username and password and inherited from AbstractUser
    # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#fields

    # personal details
    pluralSightEmail=models.CharField(_("PluralSight Email"), blank=True, max_length=255)
    pluralSightFirstName=models.CharField(_("PluralSight First Name"), blank=True, max_length=255)
    pluralSightLastName=models.CharField(_("PluralSight Last Name"), blank=True, max_length=255)

    name = models.CharField(_("Enter your name"), blank=True, max_length=255)
    bio = models.TextField(_("Bio"), blank=True, max_length=500)
    academic_qualification = models.CharField(
        _("User's highest qualification"), blank=True, max_length=30
    )
    github_profile = models.CharField(
        _("User's GitHub profile"),
        blank=True,
        max_length=255,
        validators=[validate_github_profile],
    )
    profile_image = models.ImageField(
        _("Profile image"), upload_to=user_image_path, null=True, blank=True
    )

    # users can be part of a team
    # cannot delete team if a user is part of that team
    teams = models.ForeignKey("Team", on_delete=models.PROTECT, null=True, blank=True)

    #: First and last name do not cover name patterns around the globe
    # first_name = None  # type: ignore
    # last_name = None  # type: ignore
    first_name =models.CharField(_("First Name"), blank=True, max_length=255)
    last_name =models.CharField(_("Last Name"), blank=True, max_length=255)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def github_username(self):
        split_url = self.github_profile.split("/")
        if split_url[-1] == "":
            user_name = split_url[-2]
        else:
            user_name = split_url[-1]
        return user_name


class Team(models.Model):
    """team that a user will be part of"""

    team_name = models.TextField(_("Team name"), max_length=100)


class TeamTrophyRecord(models.Model):
    """trophy records"""

    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class UserScoreCategory(models.Model):
    score_category = models.TextField(_("Score categories"), max_length=100)
    description = models.TextField(max_length=200)


class UserScore(models.Model):
    """Score connected to a user"""

    user_score_category = models.ForeignKey(UserScoreCategory, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserTrophyType(models.Model):
    score_category = models.TextField(_("Score categories"), max_length=100)
    description = models.TextField(max_length=100)


class UserTrophyRecord(models.Model):
    trophy_type = models.ForeignKey(UserTrophyType, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#TODO:Move this section to Signals.py 

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_pluralSightEmail(sender, instance, created, **kwargs):
    if created:
        User.objects.filter(pk=instance.id).update(pluralSightEmail=str(instance.id)+"@codershq.ae")
        User.objects.filter(pk=instance.id).update(pluralSightFirstName=str(instance.id))
        User.objects.filter(pk=instance.id).update(pluralSightLastName="codershq")
