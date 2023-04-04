from django.db import models

class Category(models.Model):
    CATEGORIES =(
        ("VERDURAS","VERDURAS"),
        ("CARNE","CARNE"),
        ("ASEO","ASEO"),
        ("ALACENA","ALACENA")
    )
    name = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORIES,max_length=100)

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)