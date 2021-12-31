from django.shortcuts import render
from .models import Event

# Create your views here.
def index(request):
    events = Event.objects.all().order_by('date_time')
    context = {'events': events}
    return render(request, 'events/main.html', context)
