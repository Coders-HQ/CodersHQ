from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.urls import reverse
from codershq.hackathon.models import Hackathon
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

class HackathonList(LoginRequiredMixin, ListView):
    model = Hackathon
    context_object_name = 'hackathons'
    paginate_by = 10
    ordering = ['-date_start']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class HackathonDetail(LoginRequiredMixin, DetailView):
    model = Hackathon


    def post(self, request, *args, **kwargs):

        # current hackathon instance 
        self.object = self.get_object()

        # add user if not exists
        # if user exists remove user
        if request.user in self.object.competitors.all():
            self.object.competitors.remove(request.user)
            messages.warning(request, 'You are removed from this hackathon')  

        else:
            if timezone.now().date() < self.object.last_join_date:
                self.object.competitors.add(request.user)
                messages.success(request, 'You were successfully added to the hackathon')  

        return HttpResponseRedirect(reverse('hackathon:detail', kwargs={'slug': self.object.slug}))
