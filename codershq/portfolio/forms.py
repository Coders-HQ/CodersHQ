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

class ExperienceForm(forms.Form):
    job_title = forms.CharField(max_length=50)
    start_date = forms.DateField()
    end_date = forms.DateField(required=False)
    is_current = forms.BooleanField(required=False)

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    description = forms.CharField(max_length=255, required=False)
    image = forms.ImageField(required=False)
    link = forms.URLField(required=False)
