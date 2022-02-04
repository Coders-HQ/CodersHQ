from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect, render

from codershq.users.models import User

from .forms import ParticipantForm
from .models import Event
from .utils.certificate import get_event_participants, serve_images


def index(request):
    events = Event.objects.all().order_by("date_time")
    user = request.user
    for event in events:
        if user.is_authenticated:
            if event.attendees.filter(pk=user.pk).exists():
                event.joined = True
            else:
                event.joined = False
    context = {"events": events}
    return render(request, "events/main.html", context)


@login_required
def join(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    if user.is_authenticated:
        event.attendees.add(user)
        event.save()
        messages.success(request, "Successfully joined " + event.title)

        return redirect("events:all")
    return redirect("events:all")


@login_required
def leave(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    if user.is_authenticated:
        event.attendees.remove(user)
        event.save()
        messages.success(request, "You have been removed from " + event.title)
        return redirect("events:all")
    return redirect("events:all")


@login_required
@staff_member_required
def download(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    # get all attendees and projects as a nested list
    attendee_list = get_event_participants(event)
    # get the image
    serve_images(attendee_list)

    zip_file = open("./participants.zip", "rb")
    return FileResponse(zip_file)


@staff_member_required
def participate(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":

        form = ParticipantForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]

            # get user
            user = get_object_or_404(User, email=email)

            # check if user has name
            # add name if user doesnt have
            if user.name == "":
                user.name = name

                # update db
                user.save()

            # add user to participant
            event.participants.add(user)
            event.save()

            messages.success(request, user.name + " has been added as a participant")

            # TODO: Error handling

            # clear form
            form = ParticipantForm()

    else:
        form = ParticipantForm()

    return render(request, "events/participate.html", {"form": form, "event": event})
