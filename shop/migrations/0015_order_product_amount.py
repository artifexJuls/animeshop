# Generated by Django 4.2.9 on 2024-01-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_shopcard_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
