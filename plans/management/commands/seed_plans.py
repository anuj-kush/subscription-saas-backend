from django.core.management.base import BaseCommand
from plans.models import Plan


class Command(BaseCommand):
    help = "Seed subscription plans"

    def handle(self, *args, **kwargs):

        plans = [
            {
                "name": "Free",
                "price": 0,
                "storage_limit": 1,
                "access_level": "FREE",
                "features": [
                    "Basic Dashboard",
                    "1 GB Storage"
                ],
            },
            {
                "name": "Basic",
                "price": 499,
                "storage_limit": 20,
                "access_level": "BASIC",
                "features": [
                    "Dashboard",
                    "20 GB Storage",
                    "Email Support"
                ],
            },
            {
                "name": "Premium",
                "price": 999,
                "storage_limit": 100,
                "access_level": "PREMIUM",
                "features": [
                    "Premium Dashboard",
                    "100 GB Storage",
                    "Premium Content",
                    "Priority Support"
                ],
            },
        ]

        for plan in plans:
            Plan.objects.update_or_create(
                name=plan["name"],
                defaults={
                    "price": plan["price"],
                    "storage_limit": plan["storage_limit"],
                    "access_level": plan["access_level"],
                    "features": plan["features"],
                },
            )

        self.stdout.write(
            self.style.SUCCESS("Plans seeded successfully!")
        )