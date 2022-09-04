from django.db import models
import uuid

from myapi.models.auth_models import MyUser
from myapi.models.bank_models import Bank_account

class Customer(models.Model):
    VERIFIED = 'Verified'
    REJECTED = 'Rejected'
    PENDING = 'Pending'
    APPROVAL_STATUS_CHOICES = ((VERIFIED, VERIFIED), (REJECTED, REJECTED),
                               (PENDING, PENDING))
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_number = models.CharField(null=True, unique= True,max_length=256)
    kra_pin =models.CharField(null=True, unique= True, max_length=256)
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, null= False)
    account_name = models.ForeignKey(Bank_account, on_delete=models.DO_NOTHING,null=False)
    money_recieved = models.FloatField(default=0, null=True, blank=True)
    money_withdrawn =models.FloatField(default = 0, null = True, blank=True)
   
    approval_status = models.CharField(choices=APPROVAL_STATUS_CHOICES,
                                       max_length=256,
                                       default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    @property
    def balance(self):
        current_balance = self.money_recieved - self.money_withdrawn
        return current_balance

# ----------------------------------------------------------------------------------
class MoneyTransfer(models.Model):

    MODE_CHOICES = (
        ("M-Pesa", "M-Pesa"),
        ("Card", "Card"),
        ("Wallet", "Wallet"),
    )

    SOURCE_CHOICES = (
        ("Web", "Web"),
        ("USSD", "USSD"),
        ("M-Pesa Paybill", "M-Pesa Paybill"),
    )

    ANONYMOUS = 'Anonymous'
    NAMED = 'Named'
    TYPE_CHOICES = (
        (ANONYMOUS, ANONYMOUS),
        (NAMED, NAMED),
    )
    COMPLETED = 'Completed'
    PENDING = 'Pending'
    CANCELLED = 'Cancelled'
    FAILED = 'Failed'
    STATUS_CHOICES = (
        (COMPLETED, COMPLETED),
        (PENDING, PENDING),
        (CANCELLED, CANCELLED),
        (FAILED, FAILED),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField()
    mode = models.CharField(choices=MODE_CHOICES, max_length=256, null=True)
    source = models.CharField(choices=SOURCE_CHOICES,
                              max_length=256,
                              null=True)
    phone_number = models.CharField(max_length=13, null=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=256,
                              null=True)
    transaction_reference = models.CharField(max_length=256, null=True)
    account = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self

# --------------------------------------------------------------------------------------------
class Settlement(models.Model):
    VERIFIED = 'Verified'
    PENDING = 'Pending'
    REJECTED = 'Rejected'

    STATUS_CHOICES = ((VERIFIED, VERIFIED), (PENDING, PENDING), (REJECTED,
                                                                 REJECTED))

    COMPLETED = 'Completed'
    PENDING = 'Pending'
    CANCELLED = 'Cancelled'
    FAILED = 'Failed'
    TRANSACTION_STATUS_CHOICES = (
        (COMPLETED, COMPLETED),
        (PENDING, PENDING),
        (CANCELLED, CANCELLED),
        (FAILED, FAILED),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    WithdrawalAccount=models.ForeignKey(Bank_account, on_delete=models.DO_NOTHING, null=True)
    approved = models.CharField(choices=STATUS_CHOICES,
                                max_length=256,
                                default=PENDING)
    status = models.CharField(choices=TRANSACTION_STATUS_CHOICES,
                              max_length=256,
                              null=True)
    transaction_ref = models.CharField(null=True, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

# ----------------------------------------------------------------------------------------------------------

