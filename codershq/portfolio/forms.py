from django import forms
from django.utils.translation import gettext_lazy as _

class PortfolioForm(forms.Form):
    description = forms.CharField(max_length=255)
    github_url = forms.URLField()
    linkedin_url = forms.URLField()
    website_url = forms.URLField()
    twitter_handle = forms.URLField()


