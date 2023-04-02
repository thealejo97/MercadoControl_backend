from django.db import models
from MercadoControl_Backend.users.models import User
from MercadoControl_Backend.shopping_lists.models import Shopping_list

class Shopping(models.Model):
    CURRENCY_UNIT = (
        ("COP", "COP"),
        ("USD", "USD")
    )

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_shopping')
    shoping_list = models.ForeignKey(Shopping_list, on_delete=models.CASCADE, max_length=500)

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
