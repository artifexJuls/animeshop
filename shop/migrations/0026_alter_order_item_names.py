# Generated by Django 5.0 on 2024-01-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_alter_order_item_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item_names',
            field=models.TextField(blank=True, verbose_name='Item Names'),
        ),
    ]
