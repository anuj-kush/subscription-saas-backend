from django.db import models
from django.contrib.auth.models import AbstractUser
from plans.models import Plan
from .managers import UserManager


class User(AbstractUser):

    username = None

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    current_plan = models.ForeignKey(
        Plan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self):
        return self.email