from binance.client import Client
from binance.enums import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Orders
from .serializers import OrderSerializer
from django.http import Http404


client = Client('ApiKey', 'SecretKey')
info = client.get_exchange_info() 
status = client.get_system_status()

class Order(APIView):

    """
    We Want to make a simple binance test order using Class-based Views
    """

    def get(self, request, *args, **kwargs):
        qs = Orders.objects.all()
        serializer = OrderSerializer(qs, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Buy(APIView):

    def post(self, request, *args, **kwargs):
        
        order = client.create_test_order(
            symbol=request.symbol,
            side=request.side,
            type=request.type,
            quantity=request.quantity)

        return Response(status)

class Sell(APIView):

    def post(self, request, *args, **kwargs):
        
        order = client.create_test_order(
            symbol='BNBBTC',
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=100)

        return Response(status)

class History(APIView):

    def get(self, request, *args, **kwargs):

        klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Dec, 2017")

        kline_data = []

        for i in klines:
            kline = {
                "time": i[0],
                "open": i[1],
                "high": i[2],
                "low": i[3],
                "close": i[4]
            }
        
            kline_data.append(kline)

        return Response(kline_data)
             

