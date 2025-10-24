from django.urls import include, path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

app_name = "assessment"
urlpatterns = [
    path('idp/', include('djangosaml2idp.urls', namespace='djangosaml2')),
    path('login/', LoginView.as_view(template_name='idp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(),name='logout'), #adding name
    path('', views.IndexView.as_view()),
    # App views
    path('', views.IndexView.as_view(), name='index'),  #  Only one root path
    path('assessment/', views.assessment_form, name='assessment_form'),
]
