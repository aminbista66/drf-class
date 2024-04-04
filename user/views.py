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
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)

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

        #    try:
        #        token = Token.objects.get(user=user)
        #    except Token.DoesNotExist:
        #        token = Token.objects.create(user=user)

        token, created = Token.objects.get_or_create(user=user)

        return Response({"message": "Login successful", "token": token.key})


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
