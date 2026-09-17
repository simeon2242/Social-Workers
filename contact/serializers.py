from rest_framework import serializers

from website.serializers import OptionalFieldsMixin

from .models import ContactInformation, ContactMessage


class ContactInformationSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        read_only_fields = ("created_at",)

    def validate(self, attrs):
        if self.instance is None:
            attrs["is_read"] = False
        return attrs

    def validate_full_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("Le nom complet doit contenir au moins 2 caracteres.")
        return value

    def validate_message(self, value):
        value = value.strip()
        if len(value) < 10:
            raise serializers.ValidationError("Le message doit contenir au moins 10 caracteres.")
        return value