from django.urls import path

from codershq.portfolio.views import (
    create_profile,
)

app_name = "portfolio"
urlpatterns = [
    path("", view=create_profile, name="form"),
]
