from django.urls import path

from codershq.companies.views import CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView

from . import views

app_name = "companies"
urlpatterns = [
    path('', CompanyListView.as_view(), name='company-list'),
    path('add/', CompanyCreateView.as_view(), name='company-add'),
    path('<int:pk>/', CompanyUpdateView.as_view(), name='company-update'),
    path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
]
