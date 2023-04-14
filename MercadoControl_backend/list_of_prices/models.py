from django.core.validators import RegexValidator
from django.db import models

from MercadoControl_Backend.brands.models import Brand
from MercadoControl_Backend.supermarkets.models import Supermarket
from MercadoControl_Backend.products.models import Product



class List_of_price(models.Model):
    price = models.IntegerField()
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    aditional_info = models.CharField(null=True, blank=True, max_length=500)
    picture = models.ImageField(upload_to='products/', null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


