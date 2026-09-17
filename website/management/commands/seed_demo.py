from datetime import timedelta
from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand
from django.utils import timezone
from PIL import Image, ImageDraw

from blog.models import BlogPost
from contact.models import ContactInformation, ContactMessage
from events.models import Event
from gallery.models import GalleryItem
from projects.models import Project
from team.models import TeamMember
from users.models import User
from website.models import AboutSection, CoreValue, FooterSettings, LandingPage, SiteSettings, VisionMission


class Command(BaseCommand):
    help = "Remplit une base vide avec des contenus de demonstration. Ne touche jamais a une base deja alimentee."

    def build_demo_image(self, filename, color, label):
        image = Image.new("RGB", (1200, 800), color)
        draw = ImageDraw.Draw(image)
        draw.rectangle((45, 45, 1155, 755), outline=(245, 243, 237), width=5)
        draw.text((80, 680), label, fill=(245, 243, 237))
        buffer = BytesIO()
        image.save(buffer, format="JPEG", quality=88)
        buffer.seek(0)
        return SimpleUploadedFile(filename, buffer.read(), content_type="image/jpeg")

    def handle(self, *args, **options):
        content_exists = any([
            Project.objects.exists(),
            Event.objects.exists(),
            TeamMember.objects.exists(),
            BlogPost.objects.exists(),
            GalleryItem.objects.exists(),
            VisionMission.objects.exists(),
            CoreValue.objects.exists(),
        ])
        if content_exists:
            self.stdout.write(self.style.WARNING("Contenu deja present : seed ignore pour ne pas ecraser vos modifications."))
            return

        SiteSettings.objects.get_or_create(
            pk=1,
            defaults={"organization_name": "Social Workers Forum"},
        )

        LandingPage.objects.get_or_create(
            pk=1,
            defaults={
                "title": "Construisons ensemble une societe meilleure",
                "description": "Social Workers Forum rassemble les energies, les competences et les histoires pour faire progresser une action sociale inclusive.",
                "image": self.build_demo_image("community-impact.jpg", (24, 55, 49), "COMMUNITY IMPACT"),
                "primary_button_label": "Decouvrir nos projets",
                "primary_button_url": "#projects",
                "secondary_button_label": "Nous contacter",
                "secondary_button_url": "#contact",
                "is_active": True,
            },
        )

        AboutSection.objects.get_or_create(
            pk=1,
            defaults={
                "title": "Nous croyons au pouvoir du collectif",
                "description": "Nous accompagnons les communautes et les professionnels qui agissent chaque jour pour une societe plus juste, inclusive et solidaire.",
                "image": self.build_demo_image("community-impact.jpg", (24, 55, 49), "COMMUNITY IMPACT"),
                "conclusion": "Chaque relation peut devenir un point de depart.",
                "is_active": True,
            },
        )

        vision_missions = [
            ("VISION", "Construire une societe inclusive", "Faire de chaque difference une force et de chaque voix une contribution.", "◌", 1),
            ("MISSION", "Accompagner les communautes", "Mettre en relation les personnes, les ressources et les solutions qui transforment le quotidien.", "↗", 2),
        ]
        for kind, title, description, icon, display_order in vision_missions:
            VisionMission.objects.get_or_create(
                title=title,
                defaults={"kind": kind, "description": description, "icon": icon, "display_order": display_order, "is_active": True},
            )

        values = [
            ("Solidarite", "Nous avancons ensemble, avec attention et responsabilite.", "+", 1),
            ("Inclusion", "Nous ouvrons des espaces ou chaque personne peut trouver sa place.", "◌", 2),
            ("Collaboration", "Nous croyons aux solutions construites avec les communautes.", "◎", 3),
            ("Dignite", "Nous placons la personne et son histoire au centre de chaque action.", "✦", 4),
        ]
        for title, description, icon, display_order in values:
            CoreValue.objects.get_or_create(
                title=title,
                defaults={"description": description, "icon": icon, "display_order": display_order, "is_active": True},
            )

        Project.objects.get_or_create(
            slug="jardins-solidaires",
            defaults={
                "title": "Jardins solidaires",
                "photo": self.build_demo_image("community-garden.jpg", (37, 83, 72), "COMMUNITY GARDEN"),
                "description": "Un programme participatif qui transforme des espaces urbains en lieux de rencontre, de culture et de transmission.",
                "location": "Dakar, Senegal",
                "status": Project.Status.IN_PROGRESS,
                "is_featured": True,
                "is_published": True,
                "display_order": 1,
            },
        )
        Project.objects.get_or_create(
            slug="paroles-de-jeunesse",
            defaults={
                "title": "Paroles de jeunesse",
                "photo": self.build_demo_image("youth-voices.jpg", (198, 100, 75), "YOUTH VOICES"),
                "description": "Des ateliers de parole et de creation pour permettre aux jeunes de porter leur regard sur l avenir.",
                "location": "Saint-Louis, Senegal",
                "status": Project.Status.COMPLETED,
                "is_featured": True,
                "is_published": True,
                "display_order": 2,
            },
        )

        event_date = timezone.now() + timedelta(days=21)
        event, _ = Event.objects.get_or_create(
            slug="laboratoire-action-sociale",
            defaults={
                "title": "Laboratoire d action sociale",
                "icon": "◷",
                "event_date": event_date,
                "description": "Une journee pour partager des methodes, des outils et des experiences de terrain.",
                "image": self.build_demo_image("social-lab.jpg", (113, 132, 109), "SOCIAL LAB"),
                "location": "Maison des associations",
                "is_published": True,
                "display_order": 1,
            },
        )

        TeamMember.objects.get_or_create(
            full_name="Amina Kone",
            defaults={
                "photo": self.build_demo_image("amina-kone.jpg", (217, 239, 104), "AMINA KONE"),
                "position": "Coordinatrice des programmes",
                "description": "Amina accompagne les equipes et les partenaires dans la mise en oeuvre des projets locaux.",
                "email": "amina@socialworkersforum.org",
                "phone": "+221 77 000 00 00",
                "social_links": {"linkedin": "https://linkedin.com"},
                "display_order": 1,
                "is_active": True,
            },
        )
        TeamMember.objects.get_or_create(
            full_name="Moussa Diop",
            defaults={
                "position": "Travailleur social",
                "description": "Moussa facilite les rencontres avec les communautes et les acteurs de proximite.",
                "display_order": 2,
                "is_active": True,
            },
        )

        author = User.objects.order_by("id").first()
        if author:
            BlogPost.objects.get_or_create(
                slug="ce-que-le-terrain-nous-apprend",
                defaults={
                    "title": "Ce que le terrain nous apprend",
                    "excerpt": "Trois enseignements pour construire des actions sociales plus proches des realites.",
                    "content": "Ecouter avant d agir, faire avec plutot que pour, et prendre le temps de mesurer ce qui change.",
                    "media_type": BlogPost.MediaType.IMAGE,
                    "image": self.build_demo_image("field-notes.jpg", (46, 74, 68), "FIELD NOTES"),
                    "video_url": "",
                    "author": author,
                    "published_at": timezone.now(),
                    "is_published": True,
                },
            )

        GalleryItem.objects.get_or_create(
            title="Atelier de quartier",
            defaults={
                "photo": self.build_demo_image("workshop.jpg", (197, 112, 91), "WORKSHOP"),
                "description": "Un temps d echange avec les habitants.",
                "event": event,
                "captured_at": timezone.now().date(),
                "is_active": True,
            },
        )
        GalleryItem.objects.get_or_create(
            title="Journee communautaire",
            defaults={
                "photo": self.build_demo_image("community-day.jpg", (90, 118, 105), "COMMUNITY DAY"),
                "description": "Des liens qui se construisent dans l action.",
                "event": event,
                "captured_at": timezone.now().date(),
                "is_active": True,
            },
        )

        ContactInformation.objects.get_or_create(
            pk=1,
            defaults={
                "address": "12 avenue de la Solidarite, Dakar",
                "email": "contact@socialworkersforum.org",
                "phone": "+221 33 000 00 00",
                "whatsapp_url": "https://wa.me/221330000000",
                "facebook_url": "https://facebook.com",
                "instagram_url": "https://instagram.com",
                "linkedin_url": "https://linkedin.com",
            },
        )
        FooterSettings.objects.get_or_create(
            pk=1,
            defaults={
                "description": "Une communaute de professionnels et de citoyens engages pour une action sociale plus humaine.",
                "copyright_text": "© 2026 Social Workers Forum",
                "useful_links": [{"label": "Projets", "url": "#projects"}, {"label": "Contact", "url": "#contact"}],
            },
        )
        ContactMessage.objects.get_or_create(
            full_name="Fatou Ndiaye",
            email="fatou@example.com",
            message="Je souhaite en savoir plus sur vos prochains ateliers.",
            defaults={"is_read": False},
        )

        self.stdout.write(self.style.SUCCESS("Donnees de demonstration creees avec succes."))
        self.stdout.write(f"Projets: {Project.objects.count()} | Evenements: {Event.objects.count()} | Equipe: {TeamMember.objects.count()} | Galerie: {GalleryItem.objects.count()}")