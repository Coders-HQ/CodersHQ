from django.forms import ModelForm
from codershq.challenge.models import Challenge

from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        exclude = ('owner', 'participants')
        widgets = {
            'end_date': DateInput(),
        }
