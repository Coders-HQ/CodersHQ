# Generated by Django 3.2.11 on 2022-03-18 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_task_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='education_level',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='name',
            new_name='school',
        ),
    ]