from django.urls import path

from codershq.contributor.views import (
    ContributorCreateView,
    ContributorDeleteView,
    ContributorListView,
    ContributorUpdateView,
)

app_name = "contributor"
urlpatterns = [
    path("", ContributorListView.as_view(), name="contributor-list"),
    path("<int:pk>/", ContributorUpdateView.as_view(), name="contributor-detail"),
    path("add/", ContributorCreateView.as_view(), name="contributor-add"),
    path("<int:pk>/delete/", ContributorDeleteView.as_view(), name="contributor-delete"),
]
