
from myapi.models.customer_models import Temp
from myapi.serializers.temp_serializers import TempResSerializer, TempSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
import requests

class TempView(generics.CreateAPIView):
    serializer_class = TempSerializer

    def post(self, request):
        serializer = TempSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            
            data = serializer.data
            data1=data.get('city_name')
            res=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+data1+'&appid=17a819bd1d98f912b7ba38e390e83659')
            
            json_object=res.json()
            temp = json_object['main']['temp']
            temp_degree =round((temp - 273.15))
                     
            Temperature = Temp.objects.create(
                    city_name=data.get('city_name'))
            self.serializer_class = TempResSerializer
            response_data = {}
            response_data['temp'] = temp_degree
            serialized_data = self.serializer_class(response_data)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

  

