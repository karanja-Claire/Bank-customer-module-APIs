from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from myapi.models.customer_models import MoneyTransfer, Customer, Settlement, UserRole
from myapi.serializers.customer_serializer import  CustomerReadOnly, CustomerSerializer,SettlementReadonly, SettlementSerializer
from myapi.serializers.customer_serializer import MoneytransferReadonly, MoneytransferSerializer, RoleSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

class CustomerView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'account_name']
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mode', 'account']

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

#-----------------------------------------------------------------------------------------------------------------
class SettlementView(ListCreateAPIView):
    queryset = Settlement.objects.all()
    serializer_class=SettlementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'account']
    def get_queryset(self):
        queryset = Settlement.objects.all()
        self.serializer_class = SettlementReadonly
     

        return queryset
      

    def post(self, request, format=None):
               
        serializer = SettlementSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            settle=serializer.save()
            qry = Customer.objects.filter(id=serializer.data.get('account')).first()
            if serializer.data.get('amount') <= qry.balance:              
                qry.money_withdrawn = qry.money_withdrawn + serializer.data.get(
                    'amount')
                qry.save()
                
            else:
                return Response(
                    "Cannot settle amount greater than your balance.",
                    status=status.HTTP_400_BAD_REQUEST)
            serializer = SettlementSerializer(settle)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SettlementDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SettlementSerializer
    queryset = Settlement.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter()

# ---------------------------------------------------------------------------------------------------
class RoleView(ListCreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = RoleSerializer
    def get_queryset(self):
        queryset = UserRole.objects.all()
        
   
        return queryset

    def post(self,request):
        serializer = RoleSerializer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
class RoleDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = RoleSerializer
    queryset = UserRole.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter()