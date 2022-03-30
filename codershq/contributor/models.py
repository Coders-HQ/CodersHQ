from ckeditor.fields import RichTextField
from django.db import models
from codershq.users.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField

class Contributor(models.Model):
    """Contributor model"""

    # Contributor
    name = models.CharField(_("Contributor Name"), max_length=200)
    # Role
    role = ArrayField(models.CharField(_("Roles"),max_length=200),size = 100)


    # contributor image
    image = models.ImageField(
        _("Contributor's Image"),
        upload_to="contributor/image/",
        blank=True,
        default=None,
        null=None,
    )
    #Contributor github link 
    github = models.URLField(_("Github URL"), blank=True, null=True)
    # Contributor linkedin link
    linkedin = models.URLField(_("Linkedin URL"), null=True, blank=True)

    # Contributor website url
    website = models.URLField(_("Website URL"), null=True, blank=True)

    # Contributor gitlab url
    gitlab = models.URLField(_("Gitlab URL"), null=True, blank=True)

    # Contributor twitter url
    twitter = models.URLField(_("Twitter URL"), null=True, blank=True)

   # Contributor discord url
    discord = models.URLField(_("Discord URL"), null=True, blank=True)

def __init__(self, verbose_name=None, name=None):
    return self.name

def get_absolute_url(self):
        return reverse("contributor:contributor-list")

def roles_list(self):
    response = self.role.to_array().split(',')
    print(response)
    return response

def save(self, *args, **kwargs):
        """Validate form"""
        validate_contributor(self)
        super(Contributor, self).save(*args, **kwargs)

def validate_contributor(contributor: Contributor):
  
    if name is None:
        raise ValidationError("Contributor Name needs to be specified")