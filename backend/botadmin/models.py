from django.db import models
from django.contrib.auth.models import AbstractUser


class Patient(AbstractUser):
    doctor = models.ForeignKey(
        to="self",
        symmetrical=True,
        blank=True,
    )


class Doctor(AbstractUser):
    friends = models.ManyToManyField(
        to="self",
        symmetrical=True,
        blank=True,
    )