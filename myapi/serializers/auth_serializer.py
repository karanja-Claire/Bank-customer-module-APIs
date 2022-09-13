from rest_framework import serializers
from myapi.models.auth_models import MyUser

class UserResponseSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = MyUser
        fields = [
            'id', 'username', 'email', 'phone','is_active','is_staff',
            'created_at', 'updated_at'
            
        ]

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=256, required=True)
    password = serializers.CharField(max_length=256, required=True)




class LoginResponseSerializer(serializers.Serializer):
    
    class TokensSerializer(serializers.Serializer):
        access_token = serializers.CharField(max_length=2000, required=True)
        refresh_token = serializers.CharField(max_length=2000, required=True)

    user = UserResponseSerializer()
    tokens = TokensSerializer()

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username','phone', 'email', 'password']
