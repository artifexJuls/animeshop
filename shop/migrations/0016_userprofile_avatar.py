# Generated by Django 5.0 on 2024-01-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_order_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='http://placehold.it/600x400', upload_to='media', verbose_name='Avatar'),
        ),
    ]
