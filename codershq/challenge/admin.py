from django.contrib import admin
from django.http import HttpResponse
from codershq.challenge.models import Challenge

admin.site.register(Challenge)
