# Generated by Django 4.2.9 on 2024-01-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(blank=True, max_length=500, verbose_name='Email'),
        ),
    ]
