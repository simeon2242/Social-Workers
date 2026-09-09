from django.core.validators import URLValidator
from django.db import models

from .validators import validate_image_upload


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class SiteSettings(SingletonModel):
    organization_name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="logos/", blank=True, null=True, validators=[validate_image_upload])
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=255, blank=True)
    whatsapp_url = models.URLField(blank=True, validators=[URLValidator])
    facebook_url = models.URLField(blank=True, validators=[URLValidator])
    instagram_url = models.URLField(blank=True, validators=[URLValidator])
    linkedin_url = models.URLField(blank=True, validators=[URLValidator])
    updated_at = models.DateTimeField(auto_now=True)


class LandingPage(SingletonModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="landing/", blank=True, null=True, validators=[validate_image_upload])
    primary_button_label = models.CharField(max_length=80)
    primary_button_url = models.CharField(max_length=255)
    secondary_button_label = models.CharField(max_length=80, blank=True)
    secondary_button_url = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutSection(SingletonModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="landing/", blank=True, null=True, validators=[validate_image_upload])
    conclusion = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)


class VisionMission(models.Model):
    class Kind(models.TextChoices):
        VISION = "VISION", "Vision"
        MISSION = "MISSION", "Mission"

    kind = models.CharField(max_length=10, choices=Kind.choices)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]


class CoreValue(models.Model):
    icon = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]


class FooterSettings(SingletonModel):
    description = models.TextField(blank=True)
    copyright_text = models.CharField(max_length=255, blank=True)
    useful_links = models.JSONField(default=list, blank=True)
    updated_at = models.DateTimeField(auto_now=True)