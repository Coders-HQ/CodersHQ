from django import forms

class PortfolioForm(forms.Form):
    description = forms.CharField(max_length=255, required=False)
    github_url = forms.URLField(required=False)
    linkedin_url = forms.URLField(required=False)
    website_url = forms.URLField(required=False)
    twitter_handle = forms.URLField(required=False)

class EducationForm(forms.Form):
    name = forms.CharField(max_length=50)
    education_level = forms.CharField(max_length=50)
    end_date = forms.DateField()

class UserForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    about = forms.CharField(max_length=255, required=False)
    profile_image = forms.ImageField(required=False)
