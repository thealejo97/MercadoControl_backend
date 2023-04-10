from django.db import models
from MercadoControl_Backend.users.models import User
from MercadoControl_Backend.list_of_prices.models import List_of_price

class ShoppingListListofPrice(models.Model):
    shopping_list = models.ForeignKey('shopping_lists.Shopping_list', on_delete=models.CASCADE)
    list_of_price = models.ForeignKey('list_of_prices.List_of_price', on_delete=models.CASCADE)
    estimated_price = models.IntegerField()
    amount = models.IntegerField()
    added = models.BooleanField(default=False)

class Shopping_list(models.Model):
    """
        Model that represents the shopping list, it has a list_of_prices which are the price of a product in a supermarket.
    """
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_shopping_list')

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
