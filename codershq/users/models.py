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
    name = models.CharField(_("Enter your name"), blank=True, max_length=255)
    bio = models.TextField(_("Bio"), blank=True, max_length=500)
    profile_image = models.ImageField(
        _("Profile image"), upload_to=user_image_path, null=True, blank=True
    )


    #: First and last name do not cover name patterns around the globe
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


