from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import JobProfile


@admin.register(JobProfile)
class JobProfileAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "job_status", "hourly_rate"]

    class Meta:
        verbose_name = _("codershq_model_jobprofile")
        verbose_name_plural = verbose_name
