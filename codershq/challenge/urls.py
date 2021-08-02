# urls.py
from django.urls import path
from codershq.challenge.views import ChallengeList

app_name = "challenge"
urlpatterns = [
    path('', ChallengeList.as_view(), name="list"),
]
