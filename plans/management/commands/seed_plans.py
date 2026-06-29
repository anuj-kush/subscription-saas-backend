from django.core.management.base import BaseCommand
from plans.models import Plan


class Command(BaseCommand):
    help = "Seed subscription plans"

    def handle(self, *args, **kwargs):

        plans = [
            {"name": "Free", "price": 0, "storage_limit": 1},
            {"name": "Basic", "price": 499, "storage_limit": 20},
            {"name": "Premium", "price": 999, "storage_limit": 100},
        ]

        for plan in plans:
            Plan.objects.get_or_create(
                name=plan["name"],
                defaults={
                    "price": plan["price"],
                    "storage_limit": plan["storage_limit"],
                },
            )

        self.stdout.write(
            self.style.SUCCESS("Plans seeded successfully!")
        )