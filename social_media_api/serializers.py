from django.contrib.auth import get_user_model
from rest_framework import serializers

from social_media_api.models import Post
from user.serializers import UserSerializer


class UserListSerializer(UserSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "date_of_birth",
            "age", "city",
            "country",
            "about_me"
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
