from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HackathonConfig(AppConfig):
    name = 'codershq.hackathon'
    verbose_name = _("Hackathons")

    def ready(self):
        try:
            import codershq.hackathon.signals  # noqa F401
        except ImportError:
            pass