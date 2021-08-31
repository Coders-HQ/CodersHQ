from codershq.challenge.models import SubmittedCode
from django.forms import ModelForm



class CodeSubmitForm(ModelForm):
    class Meta:
        model = SubmittedCode
        fields = ['code_file']