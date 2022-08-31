
from sre_constants import BRANCH
from rest_framework import serializers
from myapi.models.bank_models import Bank, Bank_account, Bank_branch


class BankSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(max_length=50)
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.CharField(read_only = True)
    updated_at = serializers.CharField(read_only = True)

    class Meta:
        model = Bank
        fields = [ 'bank_name','id','created_at','updated_at']

class BranchSerializer(serializers.ModelSerializer):
   
    branch_name =serializers.CharField(max_length=50)
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.CharField(read_only = True)
    updated_at = serializers.CharField(read_only = True)

    class Meta:
        model = Bank_branch
        fields = [ 'branch_name','id','bank','created_at','updated_at']

class BankAccountSerializer(serializers.ModelSerializer):
    
    account_name = serializers.CharField(max_length=50)
    account_number= serializers.CharField(max_length=50)
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.CharField(read_only = True)
    updated_at = serializers.CharField(read_only = True)

    class Meta:
        model = Bank_account
        fields = [ 'account_name','account_number','id','branch','created_at','updated_at']

# Readonly serializers for 
class BankSerializerReadonly(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class BranchSerializerReadonly(serializers.ModelSerializer):
    bank = BankSerializerReadonly()
    class Meta:
        model = Bank_branch
        fields = '__all__'

class BankAccountReadOnlySerializer(serializers.ModelSerializer):
    branch = BranchSerializerReadonly()
    class Meta:
        model = Bank_account
        fields = '__all__'

