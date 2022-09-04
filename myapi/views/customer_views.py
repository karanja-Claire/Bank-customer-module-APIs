from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from myapi.models.customer_models import MoneyTransfer, Customer
from myapi.serializers.customer_serializer import  CustomerReadOnly, CustomerSerializer, MoneytransferReadonly, MoneytransferSerializer
from rest_framework.response import Response
from rest_framework import status

class CustomerView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def get_queryset(self):
        queryset = Customer.objects.all()
        self.serializer_class = CustomerReadOnly
   
        return queryset

    def post(self,request):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            cust=serializer.save()
            serializer = CustomerReadOnly(cust)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        self.serializer_class = CustomerReadOnly
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



class CustomerDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter()
# ----------------------------------------------------------------------------------------------------------
class MoneyTransferView(ListCreateAPIView):
    queryset = MoneyTransfer.objects.all()
    serializer_class= MoneytransferSerializer

    def get_queryset(self):
        queryset = MoneyTransfer.objects.all()
        self.serializer_class = MoneytransferReadonly
        return queryset

    def post(self,request):
        serializer = MoneytransferSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            transfer=serializer.save()

            qry = Customer.objects.filter(id=serializer.data.get('account')).first()
            qry.money_recieved = qry.money_recieved + serializer.data.get(
                'amount')
            qry.save()
            serializer = MoneytransferReadonly(transfer)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        self.serializer_class = MoneytransferReadonly
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class MoneytransferDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = MoneytransferSerializer
    queryset = MoneyTransfer.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter()