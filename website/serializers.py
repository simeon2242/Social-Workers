from rest_framework import serializers

from .models import AboutSection, CoreValue, FooterSettings, LandingPage, SiteSettings, VisionMission


class OptionalFieldsMixin:
    """Rend tous les champs facultatifs (aucun champ obligatoire)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if getattr(field, "read_only", False):
                continue
            field.required = False
            if isinstance(field, serializers.CharField):
                field.allow_blank = True
            if isinstance(field, serializers.FileField):
                field.allow_null = True


class SiteSettingsSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ["id", "organization_name", "description", "email", "phone", "address", "whatsapp_url", "facebook_url", "instagram_url", "linkedin_url", "updated_at"]


class LandingPageSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = "__all__"


class AboutSectionSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = "__all__"


class VisionMissionSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = VisionMission
        fields = "__all__"

    def validate_title(self, value):
        return value.strip() if value else value


class CoreValueSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = "__all__"


class FooterSettingsSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = FooterSettings
        fields = "__all__"