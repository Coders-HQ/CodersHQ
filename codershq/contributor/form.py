from django import forms
from django.contrib.postgres.forms import SimpleArrayField


class ContributorForm(forms.Form):
    name = forms.CharField(label="Contributor Name", max_length=200)
    role = forms.SimpleArrayField(forms.CharField((label="Contributor Role (Comma Seperated)")))
    image = forms.ImageField(label="Contributor Image")
 	github = forms.URLField(label="Github URL")
 	twitter = forms.URLField(label="Twitter URL")
 	discord = forms.URLField(label="Discord URL")
 	website = forms.URLField(label="Website URL")
 	linkedin = forms.URLField(label="Linkedin URL")
 	gitlab = forms.URLField(label="Gitlab URL")
