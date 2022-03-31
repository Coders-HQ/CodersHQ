import requests
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from codershq.contributor.models import Contributor

class ContributorListView(ListView, LoginRequiredMixin):
    model = Contributor


class ContributorCreateView(CreateView):
    model = Contributor
    fields = "__all__"


class ContributorUpdateView(UpdateView):
    model = Contributor
    fields = ["name"]


class ContributorDeleteView(DeleteView):
    model = Contributor
    success_url = reverse_lazy("contributor-list")