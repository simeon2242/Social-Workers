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
    queryset = LandingPage.objects.filter(is_active=True)
    serializer_class = LandingPageSerializer


class AboutSectionViewSet(PublicContentViewSet):
    queryset = AboutSection.objects.filter(is_active=True)
    serializer_class = AboutSectionSerializer


class VisionMissionViewSet(PublicContentViewSet):
    queryset = VisionMission.objects.filter(is_active=True)
    serializer_class = VisionMissionSerializer


class CoreValueViewSet(PublicContentViewSet):
    queryset = CoreValue.objects.filter(is_active=True)
    serializer_class = CoreValueSerializer


class FooterSettingsViewSet(PublicContentViewSet):
    queryset = FooterSettings.objects.all()
    serializer_class = FooterSettingsSerializer