# Generated by Django 3.2.18 on 2023-04-08 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_lists', '0003_auto_20230408_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_list',
            name='added',
        ),
        migrations.RemoveField(
            model_name='shopping_list',
            name='estimated_price',
        ),
        migrations.RemoveField(
            model_name='shopping_list',
            name='list_of_prices',
        ),
    ]
