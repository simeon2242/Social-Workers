from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super administrateur"
        ADMIN = "ADMIN", "Administrateur"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.SUPER_ADMIN
        super().save(*args, **kwargs)