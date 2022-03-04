from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "name", "proficiency"]

    class Meta:
        verbose_name = _("codershq_model_language")
        verbose_name_plural = verbose_name
