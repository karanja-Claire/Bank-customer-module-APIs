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
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, null= False)
    account_name = models.ForeignKey(Bank_account, on_delete=models.DO_NOTHING,null=False)
    balance = models.FloatField(default=0, null=True, blank=True)
    is_active = models.BooleanField(null=True, default=True)
    approval_status = models.CharField(choices=APPROVAL_STATUS_CHOICES,
                                       max_length=256,
                                       default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)