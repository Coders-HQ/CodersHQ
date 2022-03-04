from django.db import models
from django.utils.translation import gettext_lazy as _

from codershq.portfolio.models import JobProfile


def project_image_path(self, filename):
    return "project/image/{0}/{1}".format(self.job_profile.pk, filename)


class Project(models.Model):
    job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
    name = models.CharField(_("project_field_name"), max_length=50)
    description = models.CharField(_("project_field_description"), max_length=255, null=True, blank=True)
    image = models.ImageField(_("project_field_image"), upload_to=project_image_path, blank=True, null=True)
    link = models.URLField(_("project_field_url"), null=True, blank=True)
