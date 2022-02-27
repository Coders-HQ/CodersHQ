from django.urls import path

from . import views

app_name = "portfolio"
urlpatterns = [
    path("", views.public, name="public_portfolio"),
]
