from django.urls import path

from social_media_api.views import PostListView, PostDetailView
from user.views import UserListView

urlpatterns = [
    path("profiles/", UserListView.as_view(), name="user-list"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

]
app_name = "joty"
