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

        # add user if not exists
        # if user exists remove user
        self.object = self.get_object()
        if request.user in self.object.competitors.all():
            self.object.competitors.remove(request.user)
        else:
            self.object.competitors.add(request.user)

        return HttpResponseRedirect(reverse('hackathon:detail', kwargs={'slug': self.object.slug}))
