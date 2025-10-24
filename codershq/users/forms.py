from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from codershq.users.models import UserInterest

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):

    error_message = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class PluralPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

#User Interest form for register page in the home
# codershq/users/forms.py

from django import forms
from codershq.users.models import UserInterest

class UserInterestForm(forms.ModelForm):
    class Meta:
        model = UserInterest
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Bootstrap-like styling
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-check-input'})

    def get_grouped_fields(self):
        """Return fields organized by question groups."""
        return [
            {
                "title": "1️⃣ What are you interested in?",
                "fields": [
                    ("learn", "HQ Learn"),
                    ("assessment", "HQ Assessment"),
                    ("meetups", "HQ Meetups"),
                    ("challenges", "HQ Challenges"),
                    ("hackathons", "HQ Hackathons"),
                    ("conferences", "HQ Conferences"),
                    ("get_inspired", "HQ Get Inspired"),
                    ("internship", "HQ Internship"),
                ],
            },
            {
                "title": "2️⃣ Networking",
                "fields": [
                    ("open_source", "Work collaboratively on open-source projects"),
                    ("jobs", "Job Opportunities"),
                    ("golden_visa", "Golden Visa Application"),
                    ("host_hackathon", "Request to Conduct Hackathon"),
                    ("workstation_access", "Request access to a workstation in the Coders HQ"),
                ],
            },
            {
                "title": "3️⃣ Pick Your Interests",
                "fields": [
                    ("web_dev", "Web Development"),
                    ("data_science", "Data Science"),
                    ("app_dev", "App Development"),
                    ("cloud", "Cloud Computing"),
                    ("devops", "DevOps"),
                    ("blockchain", "Blockchain Technologies"),
                    ("cybersecurity", "Cybersecurity"),
                    ("embedded_systems", "Embedded Systems"),
                ],
            },
        ]
