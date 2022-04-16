from django.urls import path

from . import views

app_name = "portfolio"
urlpatterns = [
    path("me", views.portfolio_edit, name="edit_portfolio"),
    path("me/language/delete/<int:pk>", views.portfolio_language_delete, name="delete_language_portfolio"),
    path("<str:username>", views.portfolio_show, name="show_portfolio"),
]
