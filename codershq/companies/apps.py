from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CompaniesConfig(AppConfig):
    name = 'codershq.companies'
    verbose_name = _("Companies")

    def ready(self):
        try:
            import codershq.companies.signals  # noqa F401
        except ImportError:
            pass
