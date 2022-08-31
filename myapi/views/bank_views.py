
from myapi.serializers.bank_serializer import BankAccountReadOnlySerializer, BankAccountSerializer, BankSerializer, BranchSerializer, BranchSerializerReadonly
from ..models import Bank, Bank_account, Bank_branch
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import generics



class Banks(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
    
    def get_queryset(self):
        queryset = Bank.objects.all()
        return queryset
    
    
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


class BranchView(generics.ListCreateAPIView):
    queryset = Bank_branch.objects.all()
    serializer_class = BranchSerializer
    
    
    def get_queryset(self):
        queryset = Bank_branch.objects.all()
        self.serializer_class = BranchSerializerReadonly
        return queryset
    
    
    def post(self, request, format=None):
        
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            self.serializer_class = BranchSerializerReadonly
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        self.serializer_class = BranchSerializerReadonly
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BranchSerializer
    queryset = Bank_branch.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter()


class BankAccountView(generics.ListCreateAPIView):
    queryset = Bank_account.objects.all()
    serializer_class = BankAccountSerializer
    
    
    def get_queryset(self):
        self.serializer_class = BankAccountReadOnlySerializer
        queryset = Bank_account.objects.all()
        return queryset
    
    
    def post(self, request, format=None):
        
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            self.serializer_class = BankAccountReadOnlySerializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        self.serializer_class = BankAccountReadOnlySerializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BankSerializer
    queryset = Bank_account.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter()