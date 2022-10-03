from django.urls import path

from codershq.users.views import (
    user_detail_view,
    user_redirect_view,
    user_scoring_list_view,
    user_update_view,
    plural
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("scoring/", view=user_scoring_list_view, name="scoring"),
    path("<str:username>/", view=plural, name="plural"),
]
