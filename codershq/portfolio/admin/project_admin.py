from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from codershq.portfolio.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["job_profile", "name", "description", "image", "link"]

    class Meta:
        verbose_name = _('codershq_model_project')
        verbose_name_plural = verbose_name
