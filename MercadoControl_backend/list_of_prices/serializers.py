from rest_framework import serializers
from .models import List_of_price
from ..shopping_lists.models import Shopping_list



class ListOfPriceSerializer(serializers.ModelSerializer):
    supermarket_name = serializers.SerializerMethodField(read_only=True)
    product_name = serializers.SerializerMethodField(read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = List_of_price
        fields = ['id', 'supermarket','supermarket_name', 'product','product_name','price','brand','aditional_info','picture','creation_date']

    def get_supermarket_name(self,obj):
        return obj.supermarket.name

    def get_product_name(self,obj):
        return obj.product.name + " - "+ obj.brand.name + " - " + str(obj.product.amount)