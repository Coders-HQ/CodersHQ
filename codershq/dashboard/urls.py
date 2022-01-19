# urls.py
from django.urls import path

from . import views

app_name = "dashboard"
urlpatterns = [
    # path('', TemplateView.as_view(template_name="dashboard/home.html"), name="home"),
    path("", views.index, name="home"),
    path("landing/", views.landing, name="landing"),
    path("news/", views.news, name="news"),
]
