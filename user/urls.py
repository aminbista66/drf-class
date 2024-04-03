from django.urls import path
from .views import UserListView, UserCreateView, LoginView

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("create/", UserCreateView.as_view(), name="user-create"),
]