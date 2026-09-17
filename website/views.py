from rest_framework.viewsets import ModelViewSet

from .models import AboutSection, CoreValue, FooterSettings, LandingPage, SiteSettings, VisionMission
from .permissions import IsAdminOrReadOnly
from .serializers import (
    AboutSectionSerializer,
    CoreValueSerializer,
    FooterSettingsSerializer,
    LandingPageSerializer,
    SiteSettingsSerializer,
    VisionMissionSerializer,
)


class PublicContentViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]


class SiteSettingsViewSet(PublicContentViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer


class LandingPageViewSet(PublicContentViewSet):
    serializer_class = LandingPageSerializer

    def get_queryset(self):
        queryset = LandingPage.objects.all()
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_active=True)
        return queryset


class AboutSectionViewSet(PublicContentViewSet):
    serializer_class = AboutSectionSerializer

    def get_queryset(self):
        queryset = AboutSection.objects.all()
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_active=True)
        return queryset


class VisionMissionViewSet(PublicContentViewSet):
    serializer_class = VisionMissionSerializer

    def get_queryset(self):
        queryset = VisionMission.objects.all()
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_active=True)
        return queryset


class CoreValueViewSet(PublicContentViewSet):
    serializer_class = CoreValueSerializer

    def get_queryset(self):
        queryset = CoreValue.objects.all()
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_active=True)
        return queryset


class FooterSettingsViewSet(PublicContentViewSet):
    queryset = FooterSettings.objects.all()
    serializer_class = FooterSettingsSerializer