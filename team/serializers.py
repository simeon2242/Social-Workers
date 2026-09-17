from rest_framework import serializers

from website.serializers import OptionalFieldsMixin

from .models import TeamMember


class TeamMemberSerializer(OptionalFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"

    def validate_social_links(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Les reseaux sociaux doivent etre un objet JSON.")
        return value