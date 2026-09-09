from django.db import models

from website.validators import validate_image_upload


class Project(models.Model):
    class Status(models.TextChoices):
        PLANNED = "PLANNED", "Planifie"
        IN_PROGRESS = "IN_PROGRESS", "En cours"
        COMPLETED = "COMPLETED", "Termine"
        SUSPENDED = "SUSPENDED", "Suspendu"

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    photo = models.ImageField(upload_to="projects/", validators=[validate_image_upload])
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PLANNED)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]