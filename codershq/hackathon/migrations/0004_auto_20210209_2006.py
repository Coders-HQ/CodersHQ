# Generated by Django 3.0.11 on 2021-02-09 16:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_hackathon_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
