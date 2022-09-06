from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from codershq.users.forms import UserChangeForm, UserCreationForm

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
