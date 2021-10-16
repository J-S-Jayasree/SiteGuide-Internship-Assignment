from django.db import models
from django.urls import reverse
# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vehicle_edit', kwargs={'pk': self.pk})
