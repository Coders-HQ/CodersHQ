# urls.py
from django.urls import path

from codershq.challenge.views import (
    ChallengeList, 
    ChallengeDetail,
    ChallengeCreate,
    ChallengeUpdate,
    join,
    leave)

app_name = "challenge"
urlpatterns = [
    path("", ChallengeList.as_view(), name="challenge-list"),
    path('<int:pk>/', ChallengeDetail.as_view(), name='challenge-detail'),
    path('<int:pk>/join', join, name='join'),
    path('<int:pk>/leave', leave, name='leave'),
    path("create/", ChallengeCreate.as_view(), name="challenge-create"),
    path("<int:pk>/update/", ChallengeUpdate.as_view(), name="challenge-update"),
]
