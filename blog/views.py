from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    GenericAPIView
)
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer, BlogWriteSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class BlogListView(ListAPIView):
    request: Request
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication] # this was missing and added

    def get_queryset(self):
        print(self.request.user)
        author_id = self.request.query_params.get('author_id')
        if author_id:
            return Blog.objects.filter(author__pk=author_id)
        else:
            return Blog.objects.all()

class BlogCreateView(CreateAPIView):
    serializer_class = BlogWriteSerializer  # changed this to BlogWriteSerializer

class BlogRetrieveView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDeleteView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogLikeView(GenericAPIView):
    request: Request
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        blog = Blog.objects.get(pk=kwargs.get('pk'))
        user = self.request.query_params.get('user')
        print(self.request.user)
        
        if blog.like.filter(pk=user).exists():
            blog.like.remove(user)
        else:
            blog.like.add(user)
        
        return Response({"message": "Like added successfully"})


# comment api
class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer

class CommentRetrieveView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer