
from myapi.serializers.bank_serializer import BankSerializer
from ..models import Bank
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import generics



class Banks(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
    
    def get_queryset(self):
        
        return self.queryset
    
    
    def post(self, request, format=None):
        
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BankDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter()