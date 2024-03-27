from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .seralizers import UserSerializer, UserListSerializer
from rest_framework.generics import ListAPIView, CreateAPIView

# class UserListView(APIView):
#     def get(self, request, *args, **kwargs):
#         users = User.objects.all()
#         seralizer = UserSerializer(users, many=True)
#         return Response(seralizer.data)

# class UserCreateView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({"message": "User created successfully"})

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer