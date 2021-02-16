# urls.py
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "dashboard"
urlpatterns = [
    # path('', TemplateView.as_view(template_name="dashboard/home.html"), name="home"),
    path('', views.index, name='home'),
    path('news/', views.news, name='news'),
    # path('', TemplateView.as_view(template_name="dashboard/home.html"), name="home"),
]