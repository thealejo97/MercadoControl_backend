from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)