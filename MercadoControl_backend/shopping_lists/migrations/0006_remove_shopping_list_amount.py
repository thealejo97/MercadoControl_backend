# Generated by Django 3.2.18 on 2023-04-08 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_lists', '0005_shopping_list_list_of_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_list',
            name='amount',
        ),
    ]