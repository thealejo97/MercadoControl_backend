from rest_framework import serializers
from .models import List_of_price
from ..shopping_lists.models import Shopping_list



class ListOfPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_of_price
        fields = ['id', 'supermarket', 'product']