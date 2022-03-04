from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "user_profile",
        "t_name",
        "t_description",
        "t_difficulty",
        "end_date",
    ]

    class Meta:
        verbose_name = _("codershq_model_task")
        verbose_name_plural = verbose_name
