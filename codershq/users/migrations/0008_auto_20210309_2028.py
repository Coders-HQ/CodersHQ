# Generated by Django 3.0.11 on 2021-03-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_completed_hackathons'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language_preference',
            field=models.CharField(choices=[('EN', 'English'), ('AR', 'Arabic')], default='EN', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='theme_preference',
            field=models.CharField(choices=[('LI', 'Light'), ('DA', 'Dark')], default='LI', max_length=2),
        ),
    ]
