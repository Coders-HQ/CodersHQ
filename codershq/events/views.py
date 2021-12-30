from django.shortcuts import render
from .models import Event

# Create your views here.
def index(request):
    event = Event.objects.first()
    context = {'event': event}
    return render(request, 'events/main.html', context)
