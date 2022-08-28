
from rest_framework import serializers
from myapi.models import Bank


class BankSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(max_length=50)
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.CharField(read_only = True)
    updated_at = serializers.CharField(read_only = True)

    class Meta:
        model = Bank
        fields = [ 'bank_name','id','created_at','updated_at']