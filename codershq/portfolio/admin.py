# Register your models here.
from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class AuthorAdmin(admin.ModelAdmin):
    pass