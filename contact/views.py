from rest_framework.viewsets import ModelViewSet

from website.permissions import IsContactMessageUser, IsAdminOrReadOnly

from .models import ContactInformation, ContactMessage
from .serializers import ContactInformationSerializer, ContactMessageSerializer


class ContactInformationViewSet(ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer
    permission_classes = [IsAdminOrReadOnly]


class ContactMessageViewSet(ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [IsContactMessageUser]
