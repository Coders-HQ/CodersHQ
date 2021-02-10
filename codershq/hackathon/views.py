from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.urls import reverse
from codershq.hackathon.models import Hackathon


class HackathonList(ListView):
    model = Hackathon
    context_object_name = 'hackathons'


class HackathonDetail(DetailView):
    model = Hackathon
   
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        # Look up the author we're interested in.
        self.object = self.get_object()
        self.object.competitors.add(request.user)


        return HttpResponseRedirect(reverse('hackathon:detail', kwargs={'slug': self.object.slug}))
