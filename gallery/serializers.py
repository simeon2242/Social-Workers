from rest_framework import serializers

from .models import GalleryItem


class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = "__all__"
        read_only_fields = ("created_at",)