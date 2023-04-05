from rest_framework import serializers
from .models import Shopping_list


class Shopping_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_list
        fields = ['id','name','user','amount','estimated_price','added','list_of_prices']
