from rest_framework.viewsets import ModelViewSet

from website.permissions import IsAdminOrReadOnly

from .models import Event
from .serializers import EventSerializer


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Event.objects.all()
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_published=True)
        return queryset