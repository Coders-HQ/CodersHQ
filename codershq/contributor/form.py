from django import forms
from django.forms import MultipleChoiceField
from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.postgres.fields import ArrayField

class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.

    Uses Django 1.9's postgres ArrayField
    and a MultipleChoiceField for its formfield.

    Usage:

        choices = ChoiceArrayField(models.CharField(max_length=..., choices=(...,)), default=[...])
    """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)

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
    role = ChoiceArrayField(("Roles"),
    	max_length=5000,widget=forms.SelectMultiple,
        choices=Options,default=['ui_ux_design'])
    image = forms.ImageField(label="Contributor Image")
 	github = forms.URLField(label="Github URL")
 	twitter = forms.URLField(label="Twitter URL")
 	discord = forms.URLField(label="Discord URL")
 	website = forms.URLField(label="Website URL")
 	linkedin = forms.URLField(label="Linkedin URL")
 	gitlab = forms.URLField(label="Gitlab URL")
