from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    GenericAPIView
)
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer, BlogWriteSerializer, CommentCreateSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated


class BlogListView(ListAPIView):
    request: Request
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        author_id = self.request.query_params.get('author_id')
        if author_id:
            return Blog.objects.filter(author__pk=author_id)
        else:
            return Blog.objects.all()


class BlogCreateView(CreateAPIView):
    serializer_class = BlogWriteSerializer  # changed this to BlogWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class BlogRetrieveView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# add authentication and permission
class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)
  

class BlogDeleteView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)
    

class BlogLikeView(GenericAPIView):
    request: Request
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        blog = Blog.objects.get(pk=kwargs.get('pk'))
        user = self.request.user
        
        if blog.like.filter(pk=user.pk).exists():
            blog.like.remove(user)
            return Response({"message": "Like removed successfully"})
        else:
            blog.like.add(user)
            return Response({"message": "Like added successfully"})


# comment api

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# add authentication and permission
class CommentCreateView(CreateAPIView):
    serializer_class = CommentCreateSerializer

class CommentRetrieveView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# add authentication and permission
class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

# add authentication and permission
class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer