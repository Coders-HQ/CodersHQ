from django.apps import AppConfig


class EventsConfig(AppConfig):
    name = "codershq.events"

    def ready(self):
        import codershq.events.signals #noqa