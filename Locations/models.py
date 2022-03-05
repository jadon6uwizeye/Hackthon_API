from django.db import models

class Location(models.Model):
    country = models.CharField(blank=True, max_length=255, default='Rwanda')
    province = models.CharField(blank=True, max_length=255)
    district = models.CharField(blank=True, max_length=55)
    sector = models.CharField(blank=True, max_length=55)
    cell = models.CharField(blank=True, max_length=55)
    village = models.CharField(blank=True, max_length=55)

    def __str__(self):
        return self.district
