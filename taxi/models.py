from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="cars"
    )


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"