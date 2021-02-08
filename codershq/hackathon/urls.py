# urls.py
from django.urls import path
from codershq.hackathon.views import HackathonList

app_name = "hackathon"
urlpatterns = [
    path('', HackathonList.as_view(), name="list"),
]