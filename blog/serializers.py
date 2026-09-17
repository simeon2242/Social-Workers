from rest_framework import serializers

from website.serializers import OptionalFieldsMixin

from .models import BlogPost


class BlogPostSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.get_full_name", read_only=True)

    class Meta:
        model = BlogPost
        fields = "__all__"
        read_only_fields = ("author", "created_at", "updated_at")