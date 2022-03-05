from django.db import models
from Locations.models import Location

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    address = models.ForeignKey(Location)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email