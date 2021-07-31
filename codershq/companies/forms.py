from django.forms import ModelForm
from codershq.companies.models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'website']
