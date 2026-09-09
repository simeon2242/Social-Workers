from datetime import timedelta
from pathlib import Path

from django.conf import settings
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
    help = "Creates or updates realistic demonstration content without changing the site name or logo."

    def create_demo_image(self, category, filename, color, label):
        directory = Path(settings.MEDIA_ROOT) / category
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        if not path.exists():
            image = Image.new("RGB", (1200, 800), color)
            draw = ImageDraw.Draw(image)
            draw.rectangle((45, 45, 1155, 755), outline=(245, 243, 237), width=5)
            draw.text((80, 680), label, fill=(245, 243, 237))
            image.save(path, format="JPEG", quality=88)
        return f"{category}/{filename}"

    def handle(self, *args, **options):
        image_project_1 = self.create_demo_image("projects", "community-garden.jpg", (37, 83, 72), "COMMUNITY GARDEN")
        image_project_2 = self.create_demo_image("projects", "youth-voices.jpg", (198, 100, 75), "YOUTH VOICES")
        image_event = self.create_demo_image("events", "social-lab.jpg", (113, 132, 109), "SOCIAL LAB")
        image_team = self.create_demo_image("team", "amina-kone.jpg", (217, 239, 104), "AMINA KONE")
        image_blog = self.create_demo_image("blog", "field-notes.jpg", (46, 74, 68), "FIELD NOTES")
        image_gallery_1 = self.create_demo_image("gallery", "workshop.jpg", (197, 112, 91), "WORKSHOP")
        image_gallery_2 = self.create_demo_image("gallery", "community-day.jpg", (90, 118, 105), "COMMUNITY DAY")

        site_settings, _ = SiteSettings.objects.get_or_create(
            pk=1,
            defaults={"organization_name": "Social Workers Forum"},
        )
        self.stdout.write(self.style.WARNING("Nom et logo du site preserves."))

        LandingPage.objects.update_or_create(
            pk=1,
            defaults={
                "title": "Construisons ensemble une societe meilleure",
                "description": "Social Workers Forum rassemble les energies, les competences et les histoires pour faire progresser une action sociale inclusive.",
                "image": "landing/community-impact.jpg",
                "primary_button_label": "Decouvrir nos projets",
                "primary_button_url": "#projects",
                "secondary_button_label": "Nous contacter",
                "secondary_button_url": "#contact",
                "is_active": True,
            },
        )
        self.create_demo_image("landing", "community-impact.jpg", (24, 55, 49), "COMMUNITY IMPACT")

        AboutSection.objects.update_or_create(
            pk=1,
            defaults={
                "title": "Nous croyons au pouvoir du collectif",
                "description": "Nous accompagnons les communautes et les professionnels qui agissent chaque jour pour une societe plus juste, inclusive et solidaire.",
                "image": "landing/community-impact.jpg",
                "conclusion": "Chaque relation peut devenir un point de depart.",
                "is_active": True,
            },
        )

        vision_missions = [
            ("VISION", "Construire une societe inclusive", "Faire de chaque difference une force et de chaque voix une contribution.", "◌", 1),
            ("MISSION", "Accompagner les communautes", "Mettre en relation les personnes, les ressources et les solutions qui transforment le quotidien.", "↗", 2),
        ]
        for kind, title, description, icon, display_order in vision_missions:
            VisionMission.objects.update_or_create(
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
            CoreValue.objects.update_or_create(
                title=title,
                defaults={"description": description, "icon": icon, "display_order": display_order, "is_active": True},
            )

        project_1, _ = Project.objects.update_or_create(
            slug="jardins-solidaires",
            defaults={
                "title": "Jardins solidaires",
                "photo": image_project_1,
                "description": "Un programme participatif qui transforme des espaces urbains en lieux de rencontre, de culture et de transmission.",
                "location": "Dakar, Senegal",
                "status": Project.Status.IN_PROGRESS,
                "is_featured": True,
                "is_published": True,
                "display_order": 1,
            },
        )
        Project.objects.update_or_create(
            slug="paroles-de-jeunesse",
            defaults={
                "title": "Paroles de jeunesse",
                "photo": image_project_2,
                "description": "Des ateliers de parole et de creation pour permettre aux jeunes de porter leur regard sur l avenir.",
                "location": "Saint-Louis, Senegal",
                "status": Project.Status.COMPLETED,
                "is_featured": True,
                "is_published": True,
                "display_order": 2,
            },
        )

        event_date = timezone.now() + timedelta(days=21)
        event, _ = Event.objects.update_or_create(
            slug="laboratoire-action-sociale",
            defaults={
                "title": "Laboratoire d action sociale",
                "icon": "◷",
                "event_date": event_date,
                "description": "Une journee pour partager des methodes, des outils et des experiences de terrain.",
                "image": image_event,
                "location": "Maison des associations",
                "is_published": True,
                "display_order": 1,
            },
        )

        member, _ = TeamMember.objects.update_or_create(
            full_name="Amina Kone",
            defaults={
                "photo": image_team,
                "position": "Coordinatrice des programmes",
                "description": "Amina accompagne les equipes et les partenaires dans la mise en oeuvre des projets locaux.",
                "email": "amina@socialworkersforum.org",
                "phone": "+221 77 000 00 00",
                "social_links": {"linkedin": "https://linkedin.com"},
                "display_order": 1,
                "is_active": True,
            },
        )
        TeamMember.objects.update_or_create(
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
            BlogPost.objects.update_or_create(
                slug="ce-que-le-terrain-nous-apprend",
                defaults={
                    "title": "Ce que le terrain nous apprend",
                    "excerpt": "Trois enseignements pour construire des actions sociales plus proches des realites.",
                    "content": "Ecouter avant d agir, faire avec plutot que pour, et prendre le temps de mesurer ce qui change.",
                    "media_type": BlogPost.MediaType.IMAGE,
                    "image": image_blog,
                    "video_url": "",
                    "author": author,
                    "published_at": timezone.now(),
                    "is_published": True,
                },
            )

        GalleryItem.objects.update_or_create(
            title="Atelier de quartier",
            defaults={"photo": image_gallery_1, "description": "Un temps d echange avec les habitants.", "event": event, "captured_at": timezone.now().date(), "is_active": True},
        )
        GalleryItem.objects.update_or_create(
            title="Journee communautaire",
            defaults={"photo": image_gallery_2, "description": "Des liens qui se construisent dans l action.", "event": event, "captured_at": timezone.now().date(), "is_active": True},
        )

        ContactInformation.objects.update_or_create(
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
        FooterSettings.objects.update_or_create(
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
        self.stdout.write(f"Site: {site_settings.organization_name} | Logo conserve: {bool(site_settings.logo)}")
