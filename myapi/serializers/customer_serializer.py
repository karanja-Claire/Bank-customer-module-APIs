from rest_framework import serializers
from myapi.models.customer_models import  Customer, MoneyTransfer, Settlement
from myapi.serializers.auth_serializer import UserResponseSerializer
from myapi.serializers.bank_serializer import BankAccountReadOnlySerializer


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Customer
        fields = ('id','id_number','kra_pin','account_name','user',)

class CustomerReadOnly(serializers.ModelSerializer):
    account_name = BankAccountReadOnlySerializer()
    user = UserResponseSerializer()
    class Meta:
        model = Customer
        fields =('id','id_number','kra_pin','money_recieved','money_withdrawn','balance',
        'approval_status','account_name','user','created_at','updated_at')

# ----------------------------------------------------------------------------------------------------------------
class MoneytransferSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = MoneyTransfer
        fields = ('id','account','amount')

class MoneytransferReadonly(serializers.ModelSerializer):
    account = CustomerReadOnly()
    class Meta:
        model = MoneyTransfer
        fields = '__all__'
# ------------------------------------------------------------------------------------------------------------------
class SettlementSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Settlement
        fields = ('id','account','amount')

class SettlementReadonly(serializers.ModelSerializer):
    account = CustomerReadOnly()
    class Meta:
        model = Settlement
        fields = '__all__'
