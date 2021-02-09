from django.views.generic import ListView, DetailView
from codershq.hackathon.models import Hackathon

class HackathonList(ListView):
    model = Hackathon
    context_object_name = 'hackathons'


class HackathonDetail(DetailView):
    model = Hackathon
    slug_field = "title"
    # slug_url_kwarg = "hackathon"
