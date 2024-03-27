from rest_framework import serializers
from .models import User    

# class UserSerializer(serializers.Serializer):
#     name = serializers.CharField(required=False)
#     email = serializers.EmailField()
#     password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'created_at']