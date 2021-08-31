from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.translation import gettext_lazy as _
from codershq.users.models import Team, User


class Challenge(models.Model):
    """Main challenge model"""

    name = models.CharField(_("Name of Challenge"), max_length=100)
    description = models.TextField(_("Challenge description"), max_length=5000,
                                   help_text="Describe the Challenge")
    logo = models.ImageField(_("Challenge Logo"), upload_to='challenges/logo/')
    github_link = models.TextField(_("Challenge github link"), default=None)
    website = models.TextField(_("Website link"), max_length=100)
    slack_group = models.TextField(_("Slack group"), null=True, blank=True, max_length=100)
    cloud_provider = models.TextField(_("Cloud Provider"), null=True, blank=True, max_length=100)
    cloud_provider_url = models.URLField(_("Cloud Provider URL"), null=True, blank=True)
    cloud_provider_token = models.TextField(_("Cloud Provider token"), null=True, blank=True, max_length=500)
    prticipant_teams = models.ManyToManyField(Team, blank=True)

    def __str__(self) -> str:
        return "Challenge: " + self.name

class SubmittedCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    code_file = models.FileField(upload_to='challenges/code_files/')


class Sprint(models.Model):
    """Every challenge should have at least one sprint"""

    start_date = models.DateField(_("Sprint start date"))
    end_date = models.DateField(_("Sprint end date"))
    title = models.TextField(_("Sprint title"), max_length=100)
    description = models.TextField(_("Sprint Description"), max_length=5000)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class ScoreCategory(models.Model):
    """Category of challenge scoring"""
    description = models.TextField(_("Category of challenge scoring"), max_length=100)


class SprintEnrollment(models.Model):
    """Shows which team is enrolled to which sprints"""
    team = models.ForeignKey('users.Team', on_delete=models.CASCADE)
    sprint = models.ForeignKey('Sprint', on_delete=models.CASCADE)


class ChallengeScore(models.Model):
    score_category = models.OneToOneField(ScoreCategory, on_delete=models.CASCADE)
    sprints = models.OneToOneField(Sprint, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(_("Sprint score"))
    # cannot delete team if score is associated to it
    team = models.ForeignKey('users.Team', on_delete=models.PROTECT)
