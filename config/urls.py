from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views

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
    #SSO
    path("idp/", include("djangosaml2idp.urls")),
    # Your stuff: custom urls includes go here
    path("", include("codershq.dashboard.urls", namespace="dashboard")),
    path("challenge/", include("codershq.challenge.urls", namespace="challenge")),
    path("companies/", include("codershq.companies.urls", namespace="companies")),
    path("events/", include("codershq.events.urls", namespace="events")),
    path("assessment/", include("codershq.assessment.urls", namespace="assessment")),
    path("portfolio/", include("codershq.portfolio.urls", namespace="portfolio")),

    path('api-token-auth', views.obtain_auth_token),

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
