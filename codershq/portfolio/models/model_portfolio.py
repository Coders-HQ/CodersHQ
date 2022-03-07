from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from codershq.users.models import User

CONTRIBUTOR_LEVELS = (
    (0, "None"),
    (1, "Beginner"),
    (2, "Intermediate"),
    (3, "Advanced"),
)

PROFICIENCY_LEVELS = ((1, "Beginner"), (2, "Intermediate"), (3, "Advanced"))


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


class Ambassador(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    student_email = models.EmailField(_("ambassador_field_studentEmail"))
    student_phone = models.IntegerField(_("ambassador_field_studentPhone"))
    university_name = models.CharField(_("ambassador_field_university"), max_length=60)
    responsibilities = models.CharField(
        _("ambassador_field_responsibilities"), max_length=60
    )
    start_date = models.DateField(_("ambassador_field_startDate"), default=timezone.now)
    end_date = models.DateField(_("ambassador_field_endDate"), default=timezone.now)


class Award(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(
        _("award_field_awardName"), max_length=50, null=False, blank=False
    )
    date_awarded = models.DateField(
        "award_field_awardDate", null=False, blank=False, default=timezone.now
    )


class Task(models.Model):
    t_name = models.CharField(_("task_field_name"), max_length=100)
    t_description = models.CharField(_("task_field_description"), max_length=300)
    t_difficulty = models.CharField(_("task_field_difficulty"), max_length=50)
    end_date = models.DateField(_("task_field_endDate"), default=timezone.now)

    def __str__(self):
        return "{name}".format(name=self.t_name)


class Contribution(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    contributor_role = models.CharField(_("contribution_field_role"), max_length=50)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class Education(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(
        _("education_field_name"), max_length=50, null=False, blank=False
    )
    education_level = models.CharField(
        _("education_field_educationLevel"), max_length=50, null=True, blank=True
    )
    end_date = models.DateField(_("education_field_endDate"))


class JobProfile(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    job_status = models.CharField(_("jobprofile_field_jobStatus"), max_length=50)
    hourly_rate = models.FloatField(_("jobprofile_field_hourlyRate"), default=5.0)

    def __str__(self):
        return "{name}".format(name=self.user_profile)


class Language(models.Model):
    user_profile = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(_("language_field_name"), max_length=50)
    proficiency = models.SmallIntegerField(
        _("language_field_proficiency"), choices=PROFICIENCY_LEVELS
    )
