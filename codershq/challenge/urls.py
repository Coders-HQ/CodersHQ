# urls.py
from django.urls import path

from codershq.challenge.views import ChallengeList, ChallengeDetail

app_name = "challenge"
urlpatterns = [
    path("", ChallengeList.as_view(), name="challenge-list"),
    path('<int:pk>/', ChallengeDetail.as_view(), name='challenge-detail'),
]
