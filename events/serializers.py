from rest_framework import serializers

from website.serializers import OptionalFieldsMixin

from .models import Event


class EventSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")