from django.contrib import admin
from codershq.challenge.models import Challenge, SubmittedCode

class CodeAdmin(admin.ModelAdmin):
    list_filter = ['user', 'challenge']

admin.site.register(SubmittedCode, CodeAdmin)
admin.site.register(Challenge)
