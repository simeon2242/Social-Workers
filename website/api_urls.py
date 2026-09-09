from rest_framework.routers import DefaultRouter

from blog.views import BlogPostViewSet
from contact.views import ContactInformationViewSet, ContactMessageViewSet
from events.views import EventViewSet
from gallery.views import GalleryItemViewSet
from projects.views import ProjectViewSet
from team.views import TeamMemberViewSet

from .views import (
    AboutSectionViewSet,
    CoreValueViewSet,
    FooterSettingsViewSet,
    LandingPageViewSet,
    SiteSettingsViewSet,
    VisionMissionViewSet,
)


router = DefaultRouter()
router.register("site-settings", SiteSettingsViewSet, basename="site-settings")
router.register("landing", LandingPageViewSet, basename="landing")
router.register("about", AboutSectionViewSet, basename="about")
router.register("vision-missions", VisionMissionViewSet, basename="vision-missions")
router.register("core-values", CoreValueViewSet, basename="core-values")
router.register("footer", FooterSettingsViewSet, basename="footer")
router.register("projects", ProjectViewSet, basename="projects")
router.register("events", EventViewSet, basename="events")
router.register("team", TeamMemberViewSet, basename="team")
router.register("blog", BlogPostViewSet, basename="blog")
router.register("gallery", GalleryItemViewSet, basename="gallery")
router.register("contact-information", ContactInformationViewSet, basename="contact-information")
router.register("contact/messages", ContactMessageViewSet, basename="contact-messages")