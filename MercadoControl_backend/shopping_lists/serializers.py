from django.forms import CheckboxSelectMultiple, widgets
from rest_framework import serializers
from .models import Shopping_list, ShoppingListListofPrice
from ..list_of_prices.models import List_of_price
from ..list_of_prices.serializers import ListOfPriceSerializer

class ShoppingListListofPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListListofPrice
        fields = ['list_of_price', 'estimated_price', 'amount', 'added']

class ShoppingListSerializer(serializers.ModelSerializer):
    list_of_prices = ShoppingListListofPriceSerializer(many=True,write_only=True)

    class Meta:
        model = Shopping_list
        fields = ['id', 'name', 'user', 'list_of_prices']

    def create(self, validated_data):
        list_of_prices_data = validated_data.pop('list_of_prices')
        shopping_list = Shopping_list.objects.create(**validated_data)
        for list_of_price_data in list_of_prices_data:
            ShoppingListListofPrice.objects.create(shopping_list=shopping_list, **list_of_price_data)
        return shopping_list
