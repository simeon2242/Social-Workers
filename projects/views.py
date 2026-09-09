from rest_framework.viewsets import ModelViewSet

from website.permissions import IsAdminOrReadOnly

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Project.objects.all()
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_published=True)
        return queryset