# Generated by Django 3.2.11 on 2022-09-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_pluralsightemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pluralSightFirstName',
            field=models.CharField(blank=True, max_length=255, verbose_name='PluralSight First Name'),
        ),
        migrations.AddField(
            model_name='user',
            name='pluralSightLastName',
            field=models.CharField(blank=True, max_length=255, verbose_name='PluralSight Last Name'),
        ),
    ]
