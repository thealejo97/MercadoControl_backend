from django.core.validators import RegexValidator
from django.db import models
from MercadoControl_Backend.supermarkets.models import Supermarket
from MercadoControl_Backend.products.models import Product

class ShoppingListListofPrice(models.Model):
    shopping_list = models.ForeignKey('shopping_lists.Shopping_list', on_delete=models.CASCADE)
    list_of_price = models.ForeignKey('list_of_prices.List_of_price', on_delete=models.CASCADE)
    estimated_price = models.IntegerField()
    amount = models.IntegerField()
    added = models.BooleanField(default=False)

class List_of_price(models.Model):
    price = models.IntegerField()
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_lists = models.ManyToManyField('shopping_lists.Shopping_list', through=ShoppingListListofPrice, related_name='shopping_lists')

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        name = str(self.product.name) + " , " + str(self.supermarket.name) +  " , " + str(self.price)
        return name

