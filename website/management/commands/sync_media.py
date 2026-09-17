from pathlib import Path

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Synchronise les fichiers de MEDIA_ROOT vers le stockage par defaut (ex. Backblaze B2)."

    def add_arguments(self, parser):
        parser.add_argument("--yes", action="store_true", help="Confirmer l'upload sans demander de confirmation.")

    def handle(self, *args, **options):
        base = Path(settings.MEDIA_ROOT)
        if not base.exists():
            self.stderr.write(f"Le dossier {base} n'existe pas.")
            return

        files = sorted(path for path in base.rglob("*") if path.is_file())
        pending = [
            path for path in files
            if not default_storage.exists(path.relative_to(base).as_posix())
        ]

        if not pending:
            self.stdout.write("Aucun fichier a synchroniser.")
            return

        confirm = options["yes"] or input(
            f"{len(pending)} fichier(s) a envoyer vers le stockage. Continuer ? [y/N] "
        ).strip().lower() == "y"
        if not confirm:
            self.stdout.write("Operation annulee.")
            return

        uploaded = 0
        for path in pending:
            key = path.relative_to(base).as_posix()
            with path.open("rb") as handle:
                default_storage.save(key, ContentFile(handle.read()))
            self.stdout.write(f"  ok {key}")
            uploaded += 1

        self.stdout.write(self.style.SUCCESS(f"{uploaded} fichier(s) synchronise(s) vers le stockage."))