from django import forms
from codershq.users.models import Assessment 
#class PluralPasswordForm(forms.Form):
   # password = forms.PasswordInput('password', max_length=255)
   # adding 
from django import forms

class PluralPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=255,
        label='Password'
    )

from django import forms

#adding Assesment form
class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        exclude = ['user', 'submitted_at']
