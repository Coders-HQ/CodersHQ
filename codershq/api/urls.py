from django.urls import path
from . import views
from .views import RegisterView


app_name = "api"

urlpatterns = [
    path('', views.getRoutes),
    path('register/', RegisterView.as_view(), name='auth_register'),
]

# assessment results
urlpatterns += [
    path("users/all/", views.users_all, name="users_all"),
    path("users/data/", views.users_data, name="users_data"),
    path("user/<str:username>/", views.user, name="user"),
    path("assessment/skills/all/", views.skills_all, name="skills_all"),
    path("users/skills/<int:id>/", views.user_id_skills, name="skill_id"),
    path("assessment/analytics/", views.analytics_public, name="analytics_pub"),
]
