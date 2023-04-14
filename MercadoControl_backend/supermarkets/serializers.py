from rest_framework import serializers
from .models import Supermarket


class SupermarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = ['id', 'name','phone','indicative','adress','logo_supermarket']
