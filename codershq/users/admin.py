from os import path
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from codershq.users.forms import UserChangeForm, UserCreationForm
import csv

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    actions = ['export', ]
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Profile Image"), {"fields": ("profile_image",)}),
        (_("Personal info"), {"fields": ("name", "email")}),
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
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
    
    # def get_urls(self):
    #     urls = super(UserAdmin, self).get_urls()
    #     # new_urls =[path('exportcsv/',self.export),]
    #     # return new_urls + urls


    def export(self,request,queryset):
        meta = self.model._meta

        # field names to be exported
        # use [field.name for field in meta.fields] to import all the data of specific user
        # here it only uploads the name and email 
        fieldnames = ["username","email"]

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename="UsersData.csv"'

        writer = csv.writer(response)

        writer.writerow(fieldnames) #heading in csv files

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in fieldnames])

        return response
    export.short_description ="Export to csv"
