from rest_framework.viewsets import ModelViewSet

from website.permissions import IsAdminOrReadOnly

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(ModelViewSet):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = BlogPost.objects.select_related("author")
        if self.request.user.is_anonymous:
            queryset = queryset.filter(is_published=True)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)