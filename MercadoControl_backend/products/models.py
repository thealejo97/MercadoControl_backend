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
CATEGORIES = (
    ("VERDURAS", "VERDURAS"),
    ("CARNE", "CARNE"),
    ("ASEO", "ASEO"),
    ("ALACENA", "ALACENA")
)
class Product(models.Model):

    name = models.CharField(max_length=100)
    unit_of_measure = models.CharField(choices=UNITS,max_length=100)
    amount = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORIES,max_length=100)

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        name = self.name + " - " + self.brand.name
        return name