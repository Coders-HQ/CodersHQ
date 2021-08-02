from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.urls import reverse
from codershq.challenge.models import Challenge
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class ChallengeList(LoginRequiredMixin, ListView):
    model = Challenge
    context_object_name = 'challenges'
    paginate_by = 10
    ordering = ['-date_start']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ChallengeVirtualList(LoginRequiredMixin, ListView):
    model = Challenge
    context_object_name = 'challenges'
    paginate_by = 10
    ordering = ['-date_start']

    def get_queryset(self):
        return Challenge.objects.filter(challenge_type="VI")


class ChallengePhysicalList(LoginRequiredMixin, ListView):
    model = Challenge
    context_object_name = 'challenges'
    paginate_by = 10
    ordering = ['-date_start']

    def get_queryset(self):
        return Challenge.objects.filter(challenge_type="PH")


class ChallengeHybridList(LoginRequiredMixin, ListView):
    model = Challenge
    context_object_name = 'challenges'
    paginate_by = 10
    ordering = ['-date_start']

    def get_queryset(self):
        return Challenge.objects.filter(challenge_type="HY")


class ChallengeDetail(LoginRequiredMixin, DetailView):
    model = Challenge

    def post(self, request, *args, **kwargs):

        # current challenge instance
        self.object = self.get_object()

        # add user if not exists
        # if user exists remove user
        if request.user in self.object.competitors.all():
            self.object.competitors.remove(request.user)
            messages.warning(request, 'You are removed from this challenge')

        else:
            if timezone.now().date() < self.object.last_join_date:
                self.object.competitors.add(request.user)
                messages.success(request, 'You were successfully added to the challenge')

        return HttpResponseRedirect(reverse('challenge:detail', kwargs={'slug': self.object.slug}))
