# Generated by Django 3.2.18 on 2023-04-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_lists', '0002_auto_20230405_1236'),
        ('list_of_prices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_of_price',
            name='shopping_lists',
            field=models.ManyToManyField(related_name='shopping_lists', to='shopping_lists.Shopping_list'),
        ),
    ]
