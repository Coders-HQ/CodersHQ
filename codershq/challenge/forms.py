from django import forms
from django.forms import ModelForm

from codershq.challenge.models import Challenge


class DateInput(forms.DateInput):
    input_type = "date"


def getClass(label="basic"):
    if label == "upload":
        return "block w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 cursor-pointer dark:text-gray-400 focus:outline-none focus:border-transparent dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"  # noqa
    if label == "checkbox":
        return "w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"  # noqa
    return "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  # noqa


class ChallengeForm(ModelForm):
    """Make form input pretty by using css classes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": getClass(), "type": "text"})
        self.fields["host_name"].widget.attrs.update(
            {"class": getClass(), "type": "text"}
        )
        self.fields["short_description"].widget.attrs.update({"class": getClass()})
        self.fields["is_monetary"].widget.attrs.update({"class": getClass("checkbox")})
        self.fields["image"].widget.attrs.update({"class": getClass("upload")})
        self.fields["prize_pool"].widget.attrs.update({"class": getClass()})
        self.fields["alternate_reward"].widget.attrs.update({"class": getClass()})
        self.fields["train_data"].widget.attrs.update({"class": getClass()})
        self.fields["test_data"].widget.attrs.update({"class": getClass()})
        self.fields["github_link"].widget.attrs.update({"class": getClass()})
        self.fields["website"].widget.attrs.update({"class": getClass()})
        self.fields["end_date"].widget.attrs.update({"class": getClass()})
        self.fields["gold_award"].widget.attrs.update({"class": getClass()})
        self.fields["silver_award"].widget.attrs.update({"class": getClass()})
        self.fields["bronze_award"].widget.attrs.update({"class": getClass()})
        self.fields["submission_email"].widget.attrs.update({"class": getClass()})

    class Meta:
        model = Challenge
        exclude = ("owner", "participants")
        widgets = {
            "end_date": DateInput(),
        }
