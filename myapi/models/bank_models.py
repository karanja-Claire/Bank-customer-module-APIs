from django.db import models

import uuid
from django.contrib.auth.hashers import make_password

# Create your models here.

class Bank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Bank_branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank = models.ForeignKey(Bank,
                                  on_delete=models.DO_NOTHING,
                                  null=True)
    branch_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Bank_account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_name = models.CharField(max_length=256)
    account_number = models.CharField(max_length=256)
    branch =  models.ForeignKey(Bank_branch,
                                  on_delete=models.DO_NOTHING,
                                  null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    