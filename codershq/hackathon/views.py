from django.views.generic import ListView
from codershq.hackathon.models import Hackathon

class HackathonList(ListView):
    model = Hackathon
    context_object_name = 'hackathons'


