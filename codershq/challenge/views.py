from dataclasses import field, fields
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, ListView
from .forms import ChallengeForm

from codershq.challenge.models import Challenge


class ChallengeList(LoginRequiredMixin, ListView):
    model = Challenge
    context_object_name = "challenges"
    paginate_by = 9


class ChallengeDetail(LoginRequiredMixin, DetailView):
    model = Challenge

    # def post(self, request, *args, **kwargs):

    #     # current challenge instance
    #     self.object = self.get_object()

    #     # add user if not exists
    #     # if user exists remove user
    #     if request.user in self.object.competitors.all():
    #         self.object.competitors.remove(request.user)
    #         messages.warning(request, 'You are removed from this challenge')

    #     else:
    #         if timezone.now().date() < self.object.last_join_date:
    #             self.object.competitors.add(request.user)
    #             messages.success(request, 'You were successfully added to the challenge')

    #     return HttpResponseRedirect(reverse('challenge:detail', kwargs={'slug': self.object.slug}))

# to create the challenge
class ChallengeCreate(CreateView, LoginRequiredMixin):
    template_name = 'challenge/challenge_form.html'
    form_class = ChallengeForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


@login_required
def join(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    user = request.user

    if user.is_authenticated:
        challenge.participants.add(user)
        challenge.save()
        messages.success(request, "Successfully joined " + challenge.name)

    return redirect(challenge.get_absolute_url())

@login_required
def leave(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    user = request.user

    if user.is_authenticated:
        challenge.participants.remove(user)
        challenge.save()
        messages.success(request, "Successfully left " + challenge.name)

    return redirect(challenge.get_absolute_url())