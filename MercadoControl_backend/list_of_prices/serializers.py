from rest_framework import serializers
from .models import List_of_price


class List_of_priceSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_of_price
        fields = ['id','price','supermarket','product']
