from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import Portfolio


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
