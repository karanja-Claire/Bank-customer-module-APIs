from rest_framework import serializers


class StockSerializer(serializers.Serializer):
    
    to = serializers.CharField(max_length=50)
    From= serializers.CharField(max_length=50)
    amount=serializers.CharField(max_length=50)