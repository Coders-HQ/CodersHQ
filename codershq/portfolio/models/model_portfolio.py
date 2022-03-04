from django.db import models
from django.utils.translation import gettext_lazy as _

from codershq.users.models import User

CONTRIBUTOR_LEVELS = (
    (0, "None"),
    (1, "Beginner"),
    (2, "Intermediate"),
    (3, "Advanced"),
)


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(
        _("portfolio_field_description"), max_length=255, null=True, blank=True
    )
    github_url = models.URLField(_("portfolio_field_githubUrl"), null=True, blank=True)
    linkedin_url = models.URLField(
        _("portfolio_field_linkedinUrl"), null=True, blank=True
    )
    website_url = models.URLField(
        _("portfolio_field_websiteUrl"), null=True, blank=True
    )
    twitter_handle = models.CharField(
        _("portfolio_field_twitterHandle"), null=True, blank=True, max_length=50
    )
    is_contributor = models.BooleanField(
        _("portfolio_field_isContributor"), default=False
    )
    contributor_level = models.SmallIntegerField(
        _("portfolio_field_contributorLevel"), choices=CONTRIBUTOR_LEVELS, default=0
    )
    is_admin = models.BooleanField(_("portfolio_field_isAdmin"), default=False)

    def __str__(self):
        return "{username} {name}".format(
            username=self.user.username, name=(self.user.name or "")
        )
