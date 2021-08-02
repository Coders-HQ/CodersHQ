# urls.py
from django.urls import path
from codershq.challenge.views import ChallengeList, ChallengeDetail, ChallengeVirtualList, ChallengePhysicalList, ChallengeHybridList

app_name = "challenge"
urlpatterns = [
    path('', ChallengeList.as_view(), name="list"),
    path('virtual/', ChallengeVirtualList.as_view(), name="virtual_list"),
    path('physical/', ChallengePhysicalList.as_view(), name="physical_list"),
    path('hybrid/', ChallengeHybridList.as_view(), name="hybrid_list"),
    path('<slug:slug>/', ChallengeDetail.as_view(), name="detail"),
]
