import os

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from slugify import slugify

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


def serve_images(name_project_list):

    # create image folder
    img_folder = './'
    try:
        os.mkdir(img_folder)
    except OSError:
        pass

    for name, project in name_project_list:
        file_name = slugify(name) + '.png'

        cert = Certificate('/app/staticfiles/images/certificate/empty_cert.png',name, project)
        cert.generate_certificate('/app/staticfiles/fonts/Roboto-Thin.ttf', file_name=img_folder + file_name)
    
    # cert_img.save(response, "PNG")
    # return response

def get_event_attendees(event: Event):
    """
    Returns a list of name and projects to an event
    """

    name_project_list = []

    for attendee in event.attendees.all():
        name = attendee.name

        # dont add empty name
        if name != '':
            name_project_list.append([attendee.name, event.title])

    return name_project_list
