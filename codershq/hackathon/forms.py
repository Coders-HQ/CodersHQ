from django.forms import ModelForm
from codershq.hackathon.models import Hackathon

class HackathonJoin(ModelForm):
    class Meta:
        model = Hackathon
        fields = ['competitors']
