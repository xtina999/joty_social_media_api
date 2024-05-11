from rest_framework import generics, status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from social_media_api.models import Post, Like
from social_media_api.permissions import (
    IsOwnerOrReadOnly,
    CanEditOwnProfile
)
from social_media_api.serializers import PostSerializer
from user.models import User
from user.serializers import UserSerializer


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_like(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    if not Like.objects.filter(user=user, post=post).exists():
        Like.objects.create(user=user, post=post)
        post.likes_count = Like.objects.filter(
            post=post
        ).count()
        post.save()
        return Response(
            {
                "message": "Liked"
            },
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            {
                "message": "Already liked"
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def unlike(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    like = Like.objects.filter(user=user, post=post)
    if like.exists():
        like.delete()
        post.likes_count = Like.objects.filter(post=post).count()
        post.save()  # Збереження змін
        return Response(
            {
                "message": "Unliked"
            }, status=status.HTTP_204_NO_CONTENT
        )
    else:
        return Response(
            {
                "message": "Not liked yet"
            }, status=status.HTTP_400_BAD_REQUEST
        )


class ProfileListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [CanEditOwnProfile]


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsOwnerOrReadOnly]
