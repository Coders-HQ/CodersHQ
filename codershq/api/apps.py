from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class APIConfig(AppConfig):
    name = "codershq.api"
    verbose_name = _("Api")

    def ready(self):
        try:
            import codershq.companies.signals  # noqa F401
        except ImportError:
            pass
