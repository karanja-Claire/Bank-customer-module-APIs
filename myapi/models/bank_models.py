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

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=256, unique=True)
    category_description = models.CharField(max_length=2000)
    tax_compliance_required = models.BooleanField()
    certificate_of_incorporation_required = models.BooleanField()
    kra_pin=models.BooleanField()
    id_picture_required=models.BooleanField()
    passport_photo =models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
class Bank_account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_name = models.CharField(max_length=256)
    account_number = models.CharField(max_length=256)
    category = models.ForeignKey(Category,
                                 to_field="id",null= True,related_name="category",
                                 on_delete=models.DO_NOTHING)
    branch =  models.ForeignKey(Bank_branch,
                                  on_delete=models.DO_NOTHING,
                                  null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    