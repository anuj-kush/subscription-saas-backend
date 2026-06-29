from django.db import models

class Plan(models.Model):
    PLAN_CHOICES = [
        ("Free", "Free"),
        ("Basic", "Basic"),
        ("Premium", "Premium"),
    ]

    name = models.CharField(max_length=20, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    storage_limit = models.IntegerField(help_text="Storage in GB")
    access_level = models.CharField(max_length=20)
    features = models.JSONField()

    def __str__(self):
        return self.name