from django.db import models

from events.models import Event
from website.validators import validate_image_upload


class GalleryItem(models.Model):
    photo = models.ImageField(upload_to="gallery/", validators=[validate_image_upload])
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, blank=True, null=True, related_name="gallery_items")
    captured_at = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-captured_at", "-created_at"]