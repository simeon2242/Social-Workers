from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Le titre est obligatoire.")
        return value.strip()