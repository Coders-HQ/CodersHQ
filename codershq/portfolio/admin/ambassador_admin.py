from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from codershq.portfolio.models import Ambassador


@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "student_email", "student_phone", "university_name", "start_date", "end_date"]

    class Meta:
        verbose_name = _('codershq_model_ambassador')
        verbose_name_plural = verbose_name
