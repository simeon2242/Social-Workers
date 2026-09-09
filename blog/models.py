from django.conf import settings
from django.db import models

from website.validators import validate_image_upload


class BlogPost(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = "IMAGE", "Image"
        VIDEO = "VIDEO", "Video"

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    media_type = models.CharField(max_length=10, choices=MediaType.choices, default=MediaType.IMAGE)
    image = models.ImageField(upload_to="blog/", blank=True, null=True, validators=[validate_image_upload])
    video_url = models.URLField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="blog_posts")
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]