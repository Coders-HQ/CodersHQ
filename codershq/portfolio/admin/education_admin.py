from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from codershq.portfolio.models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "name", "education_level", "end_date"]

    class Meta:
        verbose_name = _('codershq_model_education')
        verbose_name_plural = verbose_name
