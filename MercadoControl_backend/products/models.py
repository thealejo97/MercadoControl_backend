from django.db import models
from MercadoControl_Backend.brands.models import Brand
from MercadoControl_Backend.categories.models import Category

UNITS = (
    ("Kg", "Kg"),
    ("Lb", "lb"),
    ("g", "g"),
    ("L", "L"),
    ("mL", "mL"),
    ("Unidad", "Unidad"),
)
class Product(models.Model):

    name = models.CharField(max_length=100)
    unit_of_measure = models.CharField(choices=UNITS,max_length=100)
    amount = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)