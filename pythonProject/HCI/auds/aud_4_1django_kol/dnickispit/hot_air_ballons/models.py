from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# prvo od tie shto ne se zavisni


class Pilot(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    year_of_birth = models.IntegerField()
    total_hours = models.IntegerField()

    def __str__(self):
        # kako da go prikazhuva modelot (reprezentacija na modelot)
        return f"{self.first_name} {self.last_name}"


class Balloon(models.Model):
    type = models.CharField(max_length=255)
    manufacturer_name = models.CharField(max_length=255)
    max_passengers = models.IntegerField()

    def __str__(self):
        # kako da go prikazhuva modelot (reprezentacija na modelot)
        return f"{self.type}--{self.manufacturer_name}"


"""
vo baza se chuva kluch, a na korisnikot kje mu bide prikazhana vrednosta na value
(za enumeracija)
-- i za datum da vidam
"""


class Airways(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    coverage_EU = models.BooleanField()

    def __str__(self):
        # kako da go prikazhuva modelot (reprezentacija na modelot)
        return self.name

class Airways_Pilot(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE) # mora on_delete
    airways = models.ForeignKey(Airways, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pilot}--{self.airways}"


class Flight(models.Model):
    #korisnik - nadvorechen kluch do user klasata od django
    #ako e sigurno e slika -> imageField
    #txt i dr -> fileField
    code = models.CharField(max_length=255) # ako pishuva da e unikatna -> unique
    takeoff_airport = models.CharField(max_length=255)
    landing_airport = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="flights/")
    airways = models.ForeignKey(Airways, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)

#50p models, admin, views, forms itn... [total:150p]









