from django.db import models

from website.validators import validate_image_upload


class TeamMember(models.Model):
    photo = models.ImageField(upload_to="team/", blank=True, null=True, validators=[validate_image_upload])
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    social_links = models.JSONField(default=dict, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "full_name"]