from rest_framework import serializers


class TempSerializer(serializers.Serializer):
    
    city_name = serializers.CharField(max_length=50)
    
class TempResSerializer(serializers.Serializer):
    temp = serializers.CharField(max_length=50)
  
        