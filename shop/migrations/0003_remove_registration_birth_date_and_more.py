# Generated by Django 4.2.9 on 2024-01-17 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_userprofile_avatar_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='password',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='phone',
        ),
    ]
