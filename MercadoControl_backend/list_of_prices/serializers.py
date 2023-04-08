from rest_framework import serializers
from .models import List_of_price, ShoppingListListofPrice


class ShoppingListListofPriceSerializer(serializers.ModelSerializer):
    estimated_price = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = ShoppingListListofPrice
        fields = ['id', 'shopping_list', 'list_of_price', 'estimated_price', 'amount', 'added']


class List_of_priceSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    supermarket_name = serializers.CharField(source='supermarket.name')
    estimated_price = serializers.IntegerField()

    class Meta:
        model = List_of_price
        fields = ['id', 'product_name', 'supermarket_name', 'estimated_price']