# Generated by Django 3.2.18 on 2023-04-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_prices', '0004_list_of_price_shopping_lists'),
        ('shopping_lists', '0004_auto_20230408_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_list',
            name='list_of_prices',
            field=models.ManyToManyField(related_name='list_of_prices', through='list_of_prices.ShoppingListListofPrice', to='list_of_prices.List_of_price'),
        ),
    ]
