from django import forms
from django.contrib.postgres.forms import SimpleArrayField

Options = [
    ('project_management', 'Project Management'),
    ('coding', 'Coding'),
    ('ui_ux_design', 'UI/UX Design'),
    ('infrastructure', 'Infrastructure'),
    ('maintenance', 'maintenance'),
    ('content_writter', 'Content Writter'),
    ('plugin', 'Plugin'),

]


class ContributorForm(forms.Form):
    name = forms.CharField(label="Contributor Name", max_length=200)
    role = forms.MultipleChoiceField(("Roles"),
    	required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=Options)
    image = forms.ImageField(label="Contributor Image")
 	github = forms.URLField(label="Github URL")
 	twitter = forms.URLField(label="Twitter URL")
 	discord = forms.URLField(label="Discord URL")
 	website = forms.URLField(label="Website URL")
 	linkedin = forms.URLField(label="Linkedin URL")
 	gitlab = forms.URLField(label="Gitlab URL")
