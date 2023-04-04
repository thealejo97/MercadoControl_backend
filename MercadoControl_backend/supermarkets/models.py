from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Supermarket(models.Model):
    name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\d{10,15}$', message="El número de celular debe tener entre 10 y 15 dígitos.")
    phone = models.CharField(max_length=15, validators=[phone_regex], verbose_name='número de celular', null=True, blank=True)
    indicative = models.CharField(max_length=10, blank=True, null=True)
    adress = models.CharField(max_length=100, verbose_name='dirección de contacto', null=True, blank=True)


    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
