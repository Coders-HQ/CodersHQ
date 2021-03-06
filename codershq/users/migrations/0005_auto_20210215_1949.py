# Generated by Django 3.0.11 on 2021-02-15 15:49

import codershq.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=codershq.users.models.user_image_path, verbose_name='Profile image'),
        ),
    ]
