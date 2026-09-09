from pathlib import Path

from django.core.exceptions import ValidationError


ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_IMAGE_SIZE = 5 * 1024 * 1024


def validate_image_upload(upload):
    extension = Path(upload.name).suffix.lower()
    if extension not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError("Format d'image non autorise. Utilisez JPG, PNG ou WebP.")
    if upload.size > MAX_IMAGE_SIZE:
        raise ValidationError("La taille maximale d'une image est de 5 Mo.")