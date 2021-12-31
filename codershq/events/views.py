from django.shortcuts import render, get_object_or_404, redirect

from codershq import events
from .models import Event

# Create your views here.
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

    if user.is_authenticated:
        event.attendees.remove(user)
        event.save()
        print(event.attendees.all())
        return redirect('events:index')
    return redirect('events:index')