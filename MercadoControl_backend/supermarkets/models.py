from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Supermarket(models.Model):
    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='número de celular')
    indicative = models.CharField(max_length=10, blank=True, null=True)
    adress = models.CharField(max_length=100, verbose_name='dirección de contacto', null=True, blank=True)


    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name