# urls.py
from django.urls import path
from codershq.hackathon.views import HackathonList, HackathonDetail, HackathonVirtualList, HackathonPhysicalList, HackathonHybridList

app_name = "hackathon"
urlpatterns = [
    path('', HackathonList.as_view(), name="list"),
    path('virtual/', HackathonVirtualList.as_view(), name="virtual_list"),
    path('physical/', HackathonPhysicalList.as_view(), name="physical_list"),
    path('hybrid/', HackathonHybridList.as_view(), name="hybrid_list"),
    path('<slug:slug>/', HackathonDetail.as_view(), name="detail"),
]