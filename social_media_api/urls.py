from django.urls import path

from social_media_api.views import PostListView, PostDetailView, ProfileDetailView, ProfileListView

urlpatterns = [
    path("profiles/", ProfileListView.as_view(), name="user-list"),
    path("profiles/<int:pk>/", ProfileDetailView.as_view(), name="profile-detail"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

]
app_name = "joty"
