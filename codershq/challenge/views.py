from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from codershq.challenge.models import Challenge

from .forms import ChallengeForm
from .mixin import AdminStaffRequiredMixin


class ChallengeList(ListView):
    model = Challenge
    context_object_name = "challenges"
    paginate_by = 9
    ordering = ["end_date"]


class ChallengeDetail(DetailView):
    model = Challenge


class ChallengeCreate(AdminStaffRequiredMixin, CreateView):
    template_name = "challenge/challenge_form.html"
    form_class = ChallengeForm

    def form_valid(self, form):
        """save owner as the loged in user"""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ChallengeUpdate(AdminStaffRequiredMixin, UpdateView):
    template_name = "challenge/challenge_form.html"
    form_class = ChallengeForm
    model = Challenge

    # only users who are admin or owners can update
    def get(self, request, *args, **kwargs):
        if request.user != self.get_object().owner and not request.user.is_superuser:
            raise PermissionDenied
        return super().get(request, *args, **kwargs)


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
