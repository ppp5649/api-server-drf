from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")

    class Meta:
        model = Post
        fields = ["expense", "description", "author", "created_at", "updated_at"]
