from rest_framework import serializers
from .models import List_of_price
from ..shopping_lists.models import Shopping_list


class ListOfPriceSerializer(serializers.ModelSerializer):
    supermarket_name = serializers.SerializerMethodField(read_only=True)
    supermarket_logo = serializers.SerializerMethodField(read_only=True)
    product_name = serializers.SerializerMethodField(read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)
    other_prices = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = List_of_price
        fields = ['id', 'supermarket', 'supermarket_name', 'product', 'product_name', 'price', 'supermarket_logo',
                  'brand', 'aditional_info', 'picture', 'creation_date', 'other_prices']

    def get_other_prices(self, obj):
        # Si include_other_prices es False, devuelve una lista vacía
        if not obj.include_other_prices:
            return []

        # Devuelve los precios de la lista que no sean la instancia actual
        return List_of_price.objects.filter(product=obj.product).exclude(id=obj.id)

    def get_supermarket_name(self, obj):
        return obj.supermarket.name

    def get_supermarket_logo(self, obj):
        return obj.supermarket.logo_supermarket.url

    def get_product_name(self, obj):
        return obj.product.name + " - " + obj.brand.name + " - " + str(obj.product.amount) + " " + str(
            obj.product.unit_of_measure)

    def to_representation(self, instance):
        # Establece include_other_prices en True si el parámetro "include_other_prices"
        # se pasa al serializador
        include_other_prices = self.context.get('include_other_prices', False)
        instance.include_other_prices = include_other_prices
        return super().to_representation(instance)
    def get_product_name(self,obj):
        return obj.product.name + " - "+ obj.brand.name + " - " + str(obj.product.amount) + " "+ str(obj.product.unit_of_measure)
