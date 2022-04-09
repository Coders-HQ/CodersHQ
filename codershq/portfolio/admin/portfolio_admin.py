from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import (
    Ambassador,
    Award,
    Contribution,
    Education,
    JobProfile,
    Language,
    Portfolio,
    Task,
    Experience,
)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "description",
        "github_url",
        "linkedin_url",
        "is_contributor",
    ]

    class Meta:
        verbose_name = _("codershq_model_portfolio")
        verbose_name_plural = verbose_name

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [
        "user_profile",
        "job_title",
        "is_current",
        "start_date",
        "end_date",
    ]

    class Meta:
        verbose_name = _("codershq_model_experience")
        verbose_name_plural = verbose_name


@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    list_display = [
        "user_profile",
        "student_email",
        "student_phone",
        "university_name",
        "start_date",
        "end_date",
    ]

    class Meta:
        verbose_name = _("codershq_model_ambassador")
        verbose_name_plural = verbose_name


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "contributor_role", "task"]

    class Meta:
        verbose_name = _("codershq_model_task")
        verbose_name_plural = verbose_name


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "school", "degree", "end_date"]

    class Meta:
        verbose_name = _("codershq_model_education")
        verbose_name_plural = verbose_name


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "name", "date_awarded"]

    class Meta:
        verbose_name = _("codershq_model_award")
        verbose_name_plural = verbose_name


@admin.register(JobProfile)
class JobProfileAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "job_status", "hourly_rate"]

    class Meta:
        verbose_name = _("codershq_model_jobprofile")
        verbose_name_plural = verbose_name


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "name", "proficiency"]

    class Meta:
        verbose_name = _("codershq_model_language")
        verbose_name_plural = verbose_name


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "t_name",
        "t_description",
        "t_difficulty",
        "end_date",
    ]

    class Meta:
        verbose_name = _("codershq_model_task")
        verbose_name_plural = verbose_name
