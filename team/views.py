from rest_framework.viewsets import ModelViewSet

from website.permissions import IsAdminOrReadOnly

from .models import TeamMember
from .serializers import TeamMemberSerializer


class TeamMemberViewSet(ModelViewSet):
    serializer_class = TeamMemberSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = TeamMember.objects.all()
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_active=True)
        return queryset