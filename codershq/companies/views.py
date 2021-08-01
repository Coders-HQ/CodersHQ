from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from codershq.companies.models import Company

from .forms import CompanyForm


# class CompanyFormView(FormView):
#     # specify the Form you want to use
#     form_class = CompanyForm

#     # specify name of template
#     template_name = "companies/companymodel_form.html"

#     # can specify success url
#     # url to redirect after successfully
#     # updating details
#     success_url = "/thanks/"


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
