from django.urls import path

from . import views

app_name = "events"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/join/', views.join, name='join'),
]
