from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from codershq.companies.models import Company


class CompanyListView(ListView, LoginRequiredMixin):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name']


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('company-list')
