from django import forms

class PluralPasswordForm(forms.Form):
    password = forms.PasswordInput('password', max_length=255)
