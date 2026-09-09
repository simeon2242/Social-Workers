from rest_framework.viewsets import ModelViewSet

from website.permissions import IsAdminOrReadOnly

from .models import GalleryItem
from .serializers import GalleryItemSerializer


class GalleryItemViewSet(ModelViewSet):
    serializer_class = GalleryItemSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = GalleryItem.objects.select_related("event")
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_active=True)
        return queryset