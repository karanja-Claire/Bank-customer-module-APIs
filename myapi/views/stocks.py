from bank.settings import APIKEY
from myapi.models.customer_models import Temp
from myapi.serializers.stocks_serializer import StockSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
import requests
from myapi.services.stocks import StockService

class StockView(generics.CreateAPIView):
    serializer_class = StockSerializer
    stock_service = StockService()

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            
            data = serializer.data
            data1=data.get('to')
            data2=data.get('From')
            data3=data.get('Amount')
               
            res=self.stock_service.currency(to=data1,From=data2,amount=data3)
            print(res)
                   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  

