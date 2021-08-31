from codershq.challenge.forms import CodeSubmitForm
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.urls import reverse
from codershq.challenge.models import Challenge, SubmittedCode
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q


class ChallengeList(LoginRequiredMixin, TemplateView):
    template_name = 'challenge/challenge_list.html'

    def get(self, request, *args, **kwargs):
        exists = Challenge.objects.exists()
        if exists:

            #challenges = Challenge.objects.filter(prticipant_teams=request.user.teams)
            code_ids= SubmittedCode.objects.filter(user=request.user).values('challenge_id')
            submitted_challenges= Challenge.objects.filter(id__in=code_ids)
            query = Q(prticipant_teams=request.user.teams) & (~Q(id__in=code_ids))
            challenges = Challenge.objects.filter(query)
            available_challenges = Challenge.objects.exclude(prticipant_teams=request.user.teams)
            return render(request, self.template_name, {'challenges':challenges, 'available_challenges': available_challenges, 'submitted_challenges': submitted_challenges})
        else:
            return render(request, self.template_name, {'msg':'No challenges to show.'})



class ChallengeDetail(LoginRequiredMixin, TemplateView):
    template_name = 'challenge/challenge_detail.html'

    def get(self, request, id, *args, **kwargs):
        challenge = Challenge.objects.get(id=id)
        teams = challenge.prticipant_teams.all()
        user_team = request.user.teams
        query = Q(user=request.user) & Q(challenge=challenge)
        submitted = SubmittedCode.objects.filter(query).exists()

        if user_team:
            if user_team in teams:
                enrolled = True
            else:
                enrolled = False
            return render(request, self.template_name, {'challenge':challenge, 'enrolled':enrolled, 'teams':True, 'form': CodeSubmitForm, 'submitted': submitted})
        else:
            return render(request, self.template_name, {'challenge':challenge, 'teams':False})

    def post(self, request, id, *args, **kwargs):
        form = CodeSubmitForm(request.POST, request.FILES)
        challenge = Challenge.objects.get(id=id)
        if form.is_valid():
            file = request.FILES['code_file']
            user = request.user
            sc = SubmittedCode(user = user, challenge = challenge, code_file = file)
            sc.save()
        return HttpResponseRedirect(reverse('challenge:detail', args=(id,)))
        

class ChallengeEnrol(LoginRequiredMixin, TemplateView):
    template_name = 'challenge/challenge_detail.html'

    def get(self, request, id, *args, **kwargs):
        challenge = Challenge.objects.get(id=id)
        if not request.user.teams:
            return render(request, 'challenge/challenge_detail.html', {'challenge':challenge, 'teams':False})
        challenge.prticipant_teams.add(request.user.teams)
        challenge.save()
        return HttpResponseRedirect(reverse('challenge:detail', args=(id,)))


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
