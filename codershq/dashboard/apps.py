from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DashboardConfig(AppConfig):
    name = 'codershq.dashboard'

    def ready(self):
        try:
            import codershq.dashboard.signals  # noqa F401
        except ImportError:
            pass
