from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Contribution


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "contributor_role", "task"]

    class Meta:
        verbose_name = _("codershq_model_task")
        verbose_name_plural = verbose_name
