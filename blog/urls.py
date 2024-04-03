from django.urls import path
from .views import (
    BlogListView,
    BlogCreateView,
    BlogRetrieveView,
    BlogUpdateView,
    BlogDeleteView,
    CommentListView,
    CommentCreateView,
    CommentRetrieveView,
    CommentUpdateView,
    CommentDeleteView,
    BlogLikeView
)

urlpatterns = [
    path("", BlogListView.as_view()),
    path("create/", BlogCreateView.as_view()),
    path("<int:pk>/", BlogRetrieveView.as_view()),
    path("<int:pk>/update/", BlogUpdateView.as_view()),
    path("<int:pk>/delete/", BlogDeleteView.as_view()),
    path("<int:pk>/like/", BlogLikeView.as_view()),

    path("comments/", CommentListView.as_view()),
    path("comments/create/", CommentCreateView.as_view()),
    path("comments/<int:pk>/", CommentRetrieveView.as_view()),
    path("comments/<int:pk>/update/", CommentUpdateView.as_view()),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view()),
]


kwargs = {
    "pk": 1,
    "user_id": 3
}

args = (1, 3)

kwargs.get('pk')
kwargs.get('user_id')

'http://localhost:8000/blogs/1/like/?user=3&random_key=5645&random_key2=90798'