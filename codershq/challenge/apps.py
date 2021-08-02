from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChallengeConfig(AppConfig):
    name = 'codershq.challenge'
    verbose_name = _("Challenges")

    def ready(self):
        try:
            import codershq.challenge.signals  # noqa F401
        except ImportError:
            pass
