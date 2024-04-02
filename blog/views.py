from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer, BlogWriteSerializer
from rest_framework.request import Request

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

class BlogRetrieveView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDeleteView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

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