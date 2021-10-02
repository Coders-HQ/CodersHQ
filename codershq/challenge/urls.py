# urls.py
from django.urls import path
from codershq.challenge.views import ChallengeEnrol, ChallengeList, ChallengeDetail

app_name = "challenge"
urlpatterns = [
    path('', ChallengeList.as_view(), name="list"),
    path('<int:id>', ChallengeDetail.as_view(), name="detail"),
    path('submit/<int:id>', ChallengeDetail.as_view(), name="submit"),
    path('enroll/<int:id>', ChallengeEnrol.as_view(), name="enroll"),
]
