from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["job_profile", "name"]

    class Meta:
        verbose_name = _("codershq_model_service")
        verbose_name_plural = verbose_name
