

from django.urls import path

from . import views
app_name = "api"

urlpatterns = [
    path("events/", views.events, name="events"),
]
