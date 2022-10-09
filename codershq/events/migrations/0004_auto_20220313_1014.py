# Generated by Django 3.2.11 on 2022-03-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_requirements'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.CharField(default=None, max_length=140, verbose_name='Short event description'),
        ),
    ]