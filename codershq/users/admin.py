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
    
    
    def export(self,request,queryset):
        meta = self.model._meta

        # field names to be exported
        # use [field.name for field in meta.fields] to import all the data of specific user
        # here it only uploads the name and email 
        fieldnames = ["username","email"]

        response = HttpResponse(content_type='text/csv')

        # name of the file 
        response['Content-Disposition'] = 'attachment; filename="UsersData.csv"'

        # initialize the writer to write the responses in csv
        writer = csv.writer(response)

        writer.writerow(fieldnames) #heading in csv files
        
        # write each data in the csv file 
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in fieldnames])

        return response
    # short description of the of action name
    export.short_description ="Export to csv"
