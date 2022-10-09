
from django import forms
from .models import Portfolio

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ('user',)
