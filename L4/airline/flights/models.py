from django.db import models

# Create your models here.
# Get to define the models that exist,one model for each main table
# All the type of fields that exist are on the documentation

# A class called flight where we define the properties and type

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # Cascades means that if an airport is delete all flights get deleted
    # Related name allows it to work backwards
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

