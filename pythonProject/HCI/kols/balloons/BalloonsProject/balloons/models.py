from django.contrib.auth.models import User
from django.db import models

# Create your models here.

""" - settings py
import os
MEDIA_ROOT = os.path.join(BASE_DIR, "data/")
MEDIA_URL = "/data/"

i dopolnitelno app da se stavi tamu

1. django-admin startproject 'nameofproject' [e.g.mysite]
2. cd + py manage.py startapp 'nameofapp' [e.g. polls]
3. py manage.py runserver
4. in installed apps add the name of the class which is located at polls/apps.py -> e.g.'polls2.apps.Polls2Config',
5. first we need to add the models and then...
5.1 py manage.py makemigrations 'nameofapp' [e.g. polls]
[5.2] py manage.py migrate
--------------------------------
7. py manage.py createsuperuser
"""

class Pilot(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    total_hours = models.IntegerField()
    rank = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} + {self.surname}"

class Balloon(models.Model):
    balloon_type = [
        ("red", "Red"),
        ("yellow", "Yellow"),
        ("green", "Green")
    ]

    type = models.CharField(max_length=255, choices=balloon_type)
    manufacturer_name = models.CharField(max_length=255)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.type}"

class Airline(models.Model):
    name = models.CharField(max_length=255)
    year_foundation = models.IntegerField()
    outside_Europe = models.BooleanField()
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Flight(models.Model):
    code = models.CharField(max_length=255)
    airport_from = models.CharField(max_length=255)
    airport_to = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photo_flights/")
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code}"

class Collaboration(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pilot} -- {self.airline}"

