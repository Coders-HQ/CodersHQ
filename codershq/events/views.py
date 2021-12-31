from django.shortcuts import get_object_or_404, redirect, render
from PIL import Image
from django.http import HttpResponse

from codershq import events

from .models import Event
from .utils.certificate import Certificate


def index(request):
    events = Event.objects.all().order_by('date_time')
    user = request.user
    for event in events:
        if user.is_authenticated:
            if event.attendees.filter(pk=user.pk).exists():
                event.joined = True
            else:
                event.joined = False
    context = {'events': events}
    return render(request, 'events/main.html', context)


def join(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    if user.is_authenticated:
        event.attendees.add(user)
        event.save()
        return redirect('events:index')
    return redirect('events:index')


def leave(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user
    # cert = Certificate('/app/staticfiles/images/certificate/empty_cert.png','Rashed Suwaidi', 'Test Project')
    # cert_img = cert.generate_certificate('/app/staticfiles/fonts/Roboto-Thin.ttf')
    # response = HttpResponse(content_type="image/jpeg")
    # cert_img.save(response, "PNG")
    # return response

    if user.is_authenticated:
        event.attendees.remove(user)
        event.save()
        return redirect('events:index')
    return redirect('events:index')
