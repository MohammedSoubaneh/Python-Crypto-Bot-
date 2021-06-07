from rest_framework import serializers
from .models import BinanceKey, Orders, Currency

class BinanceKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceKey
        fields = ['api', 'secret']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = (
            'symbol', 'side', 'quantity', 'price'
        )