# Generated by Django 3.2.18 on 2023-04-10 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_prices', '0005_shoppinglistlistofprice_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglistlistofprice',
            name='list_of_price',
        ),
        migrations.RemoveField(
            model_name='shoppinglistlistofprice',
            name='shopping_list',
        ),
        migrations.RemoveField(
            model_name='list_of_price',
            name='shopping_lists',
        ),
    ]