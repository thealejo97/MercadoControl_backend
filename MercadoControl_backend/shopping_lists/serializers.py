from django.forms import CheckboxSelectMultiple
from rest_framework import serializers
from .models import Shopping_list
from ..list_of_prices.models import List_of_price, ShoppingListListofPrice
from ..list_of_prices.serializers import List_of_priceSerializer, ShoppingListListofPriceSerializer


class Shopping_listSerializer(serializers.ModelSerializer):
    list_of_prices = ShoppingListListofPriceSerializer(many=True)

    class Meta:
        model = Shopping_list
        fields = ['id', 'name', 'user', 'list_of_prices']

    def create(self, validated_data):
        list_of_prices_data = validated_data.pop('list_of_prices')
        shopping_list = Shopping_list.objects.create(**validated_data)
        for list_of_price_data in list_of_prices_data:
            ShoppingListListofPrice.objects.create(shopping_list=shopping_list, **list_of_price_data)
        return shopping_list
