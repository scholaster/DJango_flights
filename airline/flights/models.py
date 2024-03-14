from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} -> {self.destination} ({self.duration})"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"    
    

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class CityCountryRelation(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.IntegerField()
    area = models.FloatField()
    landmarks = models.TextField()

    def __str__(self):
        return f"{self.city} in {self.country}"
