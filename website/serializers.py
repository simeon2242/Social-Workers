from rest_framework import serializers

from .models import AboutSection, CoreValue, FooterSettings, LandingPage, SiteSettings, VisionMission


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"


class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = "__all__"


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = "__all__"


class VisionMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisionMission
        fields = "__all__"

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Le titre ne peut pas etre vide.")
        return value.strip()


class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = "__all__"


class FooterSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSettings
        fields = "__all__"