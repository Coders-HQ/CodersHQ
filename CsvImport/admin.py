from django.contrib import admin
from django.http import HttpResponse
from .models import getInfo
# from django.contrib import messages
import csv

# Register your models here.

class SaveInfo(admin.ModelAdmin):

    actions = ['export', ]

    def export(self,request,queryset):
        meta = self.model._meta

        fieldnames = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename="Responses.csv"'

        writer = csv.writer(response)

        writer.writerow(fieldnames) #heading in csv files

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in fieldnames])

        return response

    export.short_description ="Export to csv"

admin.site.register(getInfo,SaveInfo)    
