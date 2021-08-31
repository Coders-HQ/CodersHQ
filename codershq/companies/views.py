from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from codershq.companies.models import Company
from django.shortcuts import redirect, render
from .forms import CompanyCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

class CompanyListView(TemplateView, LoginRequiredMixin):
    template_name = 'companies/my_companies.html'
    def get(self, request, *args, **kwargs):
        
        exists = Company.objects.filter(user=request.user).exists()
        if exists:
            companies = Company.objects.filter(user=request.user)
            return render(request, self.template_name, {'companies':companies})
        else:
            return render(request, self.template_name, {'msg':'No companies to show.'})

class CompanyCreateView(TemplateView, LoginRequiredMixin):
    template_name = 'companies/company_form.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_company:
                return render(request, self.template_name, {'form':CompanyCreationForm})
            else:
                return render(request, 'companies/not_allowed.html')
        else:
            return render(request, 'pages/welcome.html')

    def post(self, request, *args, **kwargs):
        form = CompanyCreationForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST['name']
            logo = request.FILES['logo']
            website = request.POST['website']
            company = Company(user = request.user, name= name, logo= logo, website = website )
            company.save()
            companies = Company.objects.filter(user=request.user)
            return render(request, 'companies/my_companies.html', {'companies':companies,})
        else:
            err = form.errors
            return render(request, self.template_name, {'form':CompanyCreationForm, 'error': err,})


class CompanyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Company
    fields = ['name',
              'logo',
              'website']
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return reverse('companies:detail', kwargs={"username": self.request.user.username})


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('company-list')
