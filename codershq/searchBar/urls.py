from django.urls import path

from . import views

app_name = "searchBar"
urlpatterns = [
    path("", views.searchBar, name="searchBar"),
]
