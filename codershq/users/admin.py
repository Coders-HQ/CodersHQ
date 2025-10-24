from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from codershq.users.forms import UserChangeForm, UserCreationForm,UserInterest

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm    
    readonly_fields =('id',)

    fieldsets = (
        (None, {"fields": ("username", "password",'id')}),
        (_("PluralSight info"), {"fields": ("pluralSightEmail","pluralSightFirstName","pluralSightLastName")}),
        (_("Profile Image"), {"fields": ("profile_image",)}),
        (_("Personal info"), {"fields": ("name","first_name","last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "email","date_joined", "is_superuser"]
    search_fields = ["name"]

from django.contrib import admin
from .models import UserInterest

@admin.register(UserInterest)
class UserInterestAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "learn", "assessment", "meetups", "challenges",
        "hackathons", "conferences", "get_inspired", "internship",
        "open_source", "jobs", "golden_visa", "host_hackathon", "workstation_access",
        "web_dev", "data_science", "app_dev", "cloud", "devops",
        "blockchain", "cybersecurity", "embedded_systems",
    )
    list_filter = (
        "learn", "assessment", "meetups", "hackathons",
        "jobs", "web_dev", "data_science", "cybersecurity"
    )
    search_fields = ("user__username", "user__email")
    ordering = ("user__username",)
