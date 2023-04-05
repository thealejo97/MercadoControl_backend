from rest_framework import serializers
from .models import Shopping


class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping
        fields = ['id', 'name','user','shoping_list']
