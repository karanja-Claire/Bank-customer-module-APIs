from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import uuid
from django.contrib.auth.hashers import make_password

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email,phone,password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a email')
        if phone is None:
            raise TypeError('Users should have a phone number')
        user = self.model(username=username, email=self.normalize_email(email),phone =phone)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, email,phone, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if password is None:
            raise TypeError('Users should have a password')
        if email is None:
            raise TypeError('Users should have a email')
        if phone is None:
            raise TypeError('Users should have a phone number')
        user = self.create_user(username, email,phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class MyUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_passport_number = models.CharField(max_length=255,unique = True, null=False)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone = models.CharField(max_length=13, null=True, unique=True,blank=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','username']

    objects = UserManager()


    