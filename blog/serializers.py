from rest_framework import serializers
from .models import Blog, Comment
from user.seralizers import UserListSerializer, UserLikeSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = UserListSerializer()
    like = UserLikeSerializer(many=True)

    class Meta:
        model = Blog
        fields = '__all__'

class BlogWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'