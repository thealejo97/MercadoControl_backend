# Generated by Django 3.2.18 on 2023-04-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_prices', '0009_list_of_price_aditional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_of_price',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
