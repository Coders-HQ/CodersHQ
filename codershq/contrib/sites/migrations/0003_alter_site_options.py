# Generated by Django 3.2.11 on 2022-01-11 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20210208_2042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['domain'], 'verbose_name': 'site', 'verbose_name_plural': 'sites'},
        ),
    ]