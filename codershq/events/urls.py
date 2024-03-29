from django.urls import path

from . import views

app_name = "events"
urlpatterns = [
    path("", views.index, name="all"),
    path("<int:event_id>/", views.detail, name="event-detail"),
    path("<int:event_id>/join/", views.join, name="join"),
    path("<int:event_id>/leave/", views.leave, name="leave"),
    path("<int:event_id>/download/", views.download, name="download"),
    path("<int:event_id>/participate/", views.participate, name="participate"),
]
