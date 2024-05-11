from django.contrib.auth import get_user_model
from django.urls import reverse
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
    created_by = serializers.HyperlinkedRelatedField(
        view_name="joty:profile-detail",
        lookup_field="pk",
        read_only=True,
        format="html",
    )
    likes_count = serializers.SerializerMethodField()
    unlike = serializers.SerializerMethodField()
    add_like = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            "title",
            "text",
            "date_created",
            "hashtag",
            "created_by",
            "likes_count",
            "add_like",
            "unlike",
        )

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_add_like(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(
            reverse(
                "joty:post-add-like", kwargs={"pk": obj.pk}
            )
        )

    def get_unlike(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(
            reverse(
                "joty:post-unlike", kwargs={"pk": obj.pk}
            )
        )
