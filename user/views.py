from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .seralizers import UserSerializer, UserListSerializer, LoginSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
       serializer = LoginSerializer(data=request.data)
       if not serializer.is_valid(raise_exception=True):
           return Response({"message": "Invalid credentials"}, status=401)
       
       username = serializer.validated_data.get('username')
       password = serializer.validated_data.get('password')

        
       # This code snippet is querying the database to find a user with the provided username. Here's
       # a breakdown of what it does:
       user = User.objects.filter(username=username)
       if not user.exists():
           return Response({"message": "Invalid credentials"}, status=401)
       
       user = user.first()

       if not user.check_password(password): # type:ignore
           return Response({"message": "Invalid credentials"}, status=401)
       
       token = Token.objects.create(user=user)
       return Response({"message": "Login successful", "token": token.key})

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
