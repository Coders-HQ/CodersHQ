from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Award


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "name", "date_awarded"]

    class Meta:
        verbose_name = _('codershq_model_award')
        verbose_name_plural = verbose_name
