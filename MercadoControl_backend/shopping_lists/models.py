from django.db import models
from MercadoControl_Backend.users.models import User
from MercadoControl_Backend.list_of_prices.models import List_of_price

class Shopping_list(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_shopping_list')
    amount = models.IntegerField()
    estimated_price = models.IntegerField()
    added = models.BooleanField(default=False)
    list_of_prices = models.ForeignKey(List_of_price, on_delete=models.CASCADE, related_name='list_of_prices_shopping_list')

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
