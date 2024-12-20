from django.db import models
from django.contrib.sites.models import Site

class Organization(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name='organization')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
