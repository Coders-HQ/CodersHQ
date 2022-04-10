from django import forms

class PortfolioForm(forms.Form):
    description = forms.CharField(max_length=255, required=False)
    github_url = forms.URLField(required=False)
    linkedin_url = forms.URLField(required=False)
    website_url = forms.URLField(required=False)
    twitter_handle = forms.URLField(required=False)

class EducationForm(forms.Form):
    education_school = forms.CharField(max_length=50)
    education_degree = forms.CharField(max_length=50)
    education_start_date = forms.DateField()
    education_end_date = forms.DateField()

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
    project_name = forms.CharField(max_length=50, required=False)
    project_description = forms.CharField(max_length=255, required=False)
    project_image = forms.ImageField(required=False)
    project_url = forms.URLField(required=False)

class AwardForm(forms.Form):
    award_name = forms.CharField(max_length=50, required=False)
    award_date_awarded = forms.DateField()

class LanguageForm(forms.Form):
    language_name = forms.CharField(max_length=50, required=False)
    language_proficiency = forms.IntegerField(required=False)