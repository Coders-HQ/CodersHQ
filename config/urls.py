from allauth.account.views import confirm_email
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework_jwt.views import obtain_jwt_token
from rest_auth.views import PasswordResetConfirmView, PasswordResetView

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    path(
        "dashboard/",
        TemplateView.as_view(template_name="pages/dashboard.html"),
        name="about",
    ),
    path(
        "profile/",
        TemplateView.as_view(template_name="pages/profile.html"),
        name="about",
    ),
    path(
        "construction/",
        TemplateView.as_view(template_name="pages/underConstruction.html"),
        name="construction",
    ),
    path(
        "comingSoon/",
        TemplateView.as_view(template_name="pages/comingSoon.html"),
        name="comingSoon",
    ),
    path(
        "comingSoon2/",
        TemplateView.as_view(template_name="pages/comingSoon2.html"),
        name="comingSoon2",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("codershq.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # SSO
    path("idp/", include("djangosaml2idp.urls")),
    # Your stuff: custom urls includes go here
    path("", include("codershq.dashboard.urls", namespace="dashboard")),
    path("challenge/", include("codershq.challenge.urls", namespace="challenge")),
    path("companies/", include("codershq.companies.urls", namespace="companies")),
    path("events/", include("codershq.events.urls", namespace="events")),
    path("assessment/", include("codershq.assessment.urls", namespace="assessment")),
    path("portfolio/", include("codershq.portfolio.urls", namespace="portfolio")),

    #  API
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('rest-auth/password/reset/', PasswordResetView.as_view(), name='rest_password_reset',),
    path('rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm',),

    path('api-token-auth/', obtain_jwt_token),
    path("api/", include("codershq.api.urls", namespace="api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
