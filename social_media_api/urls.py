from django.urls import path

from social_media_api.views import (
    PostListView,
    PostDetailView,
    ProfileDetailView,
    ProfileListView,
    add_like,
    unlike
)

urlpatterns = [
    path("profiles/", ProfileListView.as_view(), name="user-list"),
    path(
        "profiles/<int:pk>/",
        ProfileDetailView.as_view(),
        name="profile-detail"
    ),
    path("posts/", PostListView.as_view(), name="post-list"),
    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path("posts/<int:pk>/like/", add_like, name="post-add-like"),
    path("posts/<int:pk>/unlike/", unlike, name="post-unlike"),

]
app_name = "joty"
