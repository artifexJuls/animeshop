# Generated by Django 4.2.9 on 2024-01-17 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_userprofile_avatar_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
    ]
