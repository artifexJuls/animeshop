# Generated by Django 5.0 on 2024-01-18 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_userprofile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
    ]