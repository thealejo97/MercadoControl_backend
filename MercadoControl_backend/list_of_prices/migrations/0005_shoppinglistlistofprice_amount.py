# Generated by Django 3.2.18 on 2023-04-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_prices', '0004_list_of_price_shopping_lists'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglistlistofprice',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
