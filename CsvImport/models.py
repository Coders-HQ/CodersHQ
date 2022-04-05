from django.db import models
# Create your models here.
class getInfo(models.Model):

    object = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
