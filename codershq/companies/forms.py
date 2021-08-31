from django.forms import ModelForm
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

from .models import Company

class CompanyCreationForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'website']
