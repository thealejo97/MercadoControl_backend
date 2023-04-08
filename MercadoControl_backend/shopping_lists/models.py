from django.db import models
from MercadoControl_Backend.users.models import User
from MercadoControl_Backend.list_of_prices.models import List_of_price, ShoppingListListofPrice

class Shopping_list(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_shopping_list')
    list_of_prices = models.ManyToManyField(List_of_price, through=ShoppingListListofPrice, related_name='list_of_prices')

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
