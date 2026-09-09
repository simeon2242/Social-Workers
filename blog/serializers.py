from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.get_full_name", read_only=True)

    class Meta:
        model = BlogPost
        fields = "__all__"
        read_only_fields = ("author", "created_at", "updated_at")

    def validate(self, attrs):
        media_type = attrs.get("media_type", getattr(self.instance, "media_type", BlogPost.MediaType.IMAGE))
        image = attrs.get("image", getattr(self.instance, "image", None))
        video_url = attrs.get("video_url", getattr(self.instance, "video_url", ""))
        if media_type == BlogPost.MediaType.IMAGE and not image:
            raise serializers.ValidationError({"image": "Une image est requise pour un article de type IMAGE."})
        if media_type == BlogPost.MediaType.VIDEO and not video_url:
            raise serializers.ValidationError({"video_url": "Une URL vidéo est requise pour un article de type VIDEO."})
        return attrs