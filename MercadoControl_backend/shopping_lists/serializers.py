from django.forms import CheckboxSelectMultiple, widgets
from rest_framework import serializers
from .models import Shopping_list, ShoppingListListofPrice
from ..list_of_prices.models import List_of_price
from ..list_of_prices.serializers import ListOfPriceSerializer

class ShoppingListListofPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListListofPrice
        fields = ['list_of_price', 'estimated_price', 'amount', 'added']

class ShoppingListListofPriceSerializerReading(serializers.ModelSerializer):
    list_of_price = ListOfPriceSerializer()
    class Meta:
        model = ShoppingListListofPrice
        fields = ['list_of_price', 'estimated_price', 'amount', 'added']

class ShoppingListSerializer(serializers.ModelSerializer):
    list_of_prices = ShoppingListListofPriceSerializer(many=True, write_only=True)
    products_of_shopping_list = serializers.SerializerMethodField()

    class Meta:
        model = Shopping_list
        fields = ['id', 'name', 'user', 'list_of_prices','products_of_shopping_list']

    def create(self, validated_data):
        list_of_prices_data = validated_data.pop('list_of_prices')
        shopping_list = Shopping_list.objects.create(**validated_data)
        for list_of_price_data in list_of_prices_data:
            ShoppingListListofPrice.objects.create(shopping_list=shopping_list, **list_of_price_data)
        return shopping_list

    # def get_related_list_of_prices(self, obj):
    #     shopping_list_related = ShoppingListListofPrice.objects.filter(shopping_list=obj.id)
    #     querysetList_of_price = List_of_price.objects.none()
    #     for sh in shopping_list_related:
    #         querysetList_of_price |= List_of_price.objects.filter(id=sh.list_of_price.id)
    #     serializer = ListOfPriceSerializer(querysetList_of_price, many=True)
    #     return serializer.data
    def get_products_of_shopping_list(self, obj):
        shopping_list_related = ShoppingListListofPrice.objects.filter(shopping_list=obj.id)

        serializer = ShoppingListListofPriceSerializerReading(shopping_list_related, many=True)
        return serializer.data