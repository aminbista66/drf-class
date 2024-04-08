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
    
    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        
        user.set_password(password)
        user.save()
        return user



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']

class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)