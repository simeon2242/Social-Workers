from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    help = "Creates or updates the superuser and forces its password (idempotent)."

    def add_arguments(self, parser):
        parser.add_argument("--username", required=True)
        parser.add_argument("--password", required=True)
        parser.add_argument("--email", default="")

    def handle(self, *args, **options):
        username = options["username"]
        password = options["password"]
        email = options["email"]

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.email = email or user.email
        user.set_password(password)
        user.save()

        message = f"Superuser '{username}' created." if created else f"Superuser '{username}' password updated."
        self.stdout.write(self.style.SUCCESS(message))