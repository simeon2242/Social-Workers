from django.db import models

from website.validators import validate_image_upload


class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    icon = models.CharField(max_length=100, blank=True)
    event_date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to="events/", blank=True, null=True, validators=[validate_image_upload])
    location = models.CharField(max_length=255, blank=True)
    is_published = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["event_date", "display_order"]