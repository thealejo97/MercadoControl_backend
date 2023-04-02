from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

class User(AbstractBaseUser):
    CURRENCY_UNIT = (
        ("COP", "COP"),
        ("USD", "USD")
    )

    currency_unit = models.CharField(max_length=50, choices=CURRENCY_UNIT)
    phone_regex = RegexValidator(regex=r'^\d{10,15}$', message="El número de celular debe tener entre 10 y 15 dígitos.")
    phone = models.CharField(max_length=15, validators=[phone_regex], verbose_name='número de celular', null=True, blank=True)
    indicative = models.CharField(max_length=10, blank=True, null=True)
    adress = models.CharField(max_length=100, verbose_name='dirección de contacto', null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
