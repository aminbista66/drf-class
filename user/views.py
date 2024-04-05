from rest_framework.views import APIView
from rest_framework.response import Response


from .models import User


from .seralizers import (
    UserSerializer,
    UserListSerializer,
    LoginSerializer,
    LogoutSerializer,
)


from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=401)

        if not user.check_password(password):  # type:ignore
            return Response({"message": "Invalid credentials"}, status=401)

        token, created = Token.objects.get_or_create(user=user)

        return Response({"message": "Login successful", "token": token.key})


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token_from_user = serializer.validated_data.get("token")

        try:
            token = Token.objects.get(key=token_from_user)
            token.delete()
            return Response({"message": "Logout successful"}, status=200)
        
        except Token.DoesNotExist:
            return Response({"message": "Invalid token"}, status=400)
        

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
