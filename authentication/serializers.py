from rest_framework import serializers
from authentication.models import CustomUser
from rest_framework import validators
from django.core.validators import validate_email

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120, min_length=6, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        
    def create(self, validated_data):
        
        return CustomUser.objects.create_user(**validated_data)
            
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120, min_length=6, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'token']
        read_only_fields = ['token', ]