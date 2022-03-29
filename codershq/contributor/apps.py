from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContributorConfig(AppConfig):
     name = "codershq.contributor"
     verbose_name = _("Contributors")

def ready(self):
        try:
            import codershq.contributor.signals  # noqa F401
        except ImportError:
            pass
