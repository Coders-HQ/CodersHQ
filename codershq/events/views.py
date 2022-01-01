import os

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from slugify import slugify

from .models import Event
from .utils.certificate import Certificate, serve_images, get_event_attendees


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


@login_required
def join(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    if user.is_authenticated:
        event.attendees.add(user)
        event.save()
        return redirect('events:index')
    return redirect('events:index')


@login_required
def leave(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    if user.is_authenticated:
        event.attendees.remove(user)
        event.save()
        return redirect('events:index')
    return redirect('events:index')


@login_required
@staff_member_required
def download(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    attendee_list = get_event_attendees(event)
    serve_images(attendee_list)

    return redirect('events:index')


