from django.core import serializers
from django.http import JsonResponse

from codershq.events.models import Event


def events(request):
    events = Event.objects.all()
    data = serializers.serialize(
        "json",
        events,
        fields=[
            "name",
            "short_description",
            "start",
            "image",
            "link",
        ],
    )

    return JsonResponse(data, safe=False)
