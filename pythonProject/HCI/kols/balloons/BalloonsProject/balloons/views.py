


"""
VIEWS

from django.shortcuts import render

# Create your views here.
from . import forms
from .models import *



def index(request):
    return render(request, "index.html")

def flights(request):
    if request.method == "POST":
        form_data = forms.FlightForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            flight = form_data.save(commit=False)
            flight.user = request.user
            flight.image = form_data.cleaned_data["image"]
            flight.save()

    context = {
        "flights": Flight.objects.filter(user=request.user, airport_from="Skopje").all(),
        "form": forms.FlightForm
    }
    return render(request, "flights.html", context=context)


vo head
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
getbootstrap.com 

FORMS

from django import forms
from .models import *


class FlightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.visible_fields():
            f.field.widgets.attrs["class"] = "form-control"

    class Meta:
        model = Flight
        exclude = ["user",]





MODELS

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
"""
""" - settings py
import os
MEDIA_ROOT = os.path.join(BASE_DIR, "data/")
MEDIA_URL = "/data/"

i dopolnitelno app da se stavi tamu vo installed apps

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

"""
"""
"""

"""
urls 
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from balloons import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('flights/', views.flights, name="flights")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
"""
flights.html

{% for f in flights %}
<div>
  <div class="card" style="width: 18rem;">
  <img src="{{MEDIA_URL}} {{f.photo}}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">{{f.code}}</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Click for more info</a>
  </div>
</div>
</div>

<form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form }}
        <button type="submit" class="btn btn-success mt-3">Submit</button>
    </form>

<form>
{{form}}}
  <button></button>
</form>
{% endfor %}

=============
<li class="nav-item">
          <a class="nav-link" href="{% url 'index' %}">Index</a>
        </li>
"""

"""
admin

from django.contrib import admin

# Register your models here.

from .models import *

class CollaborationAdmin(admin.TabularInline):
    model = Collaboration
    extra = 1

class AirlineAdmin(admin.ModelAdmin):
    inlines = [CollaborationAdmin,]
    list_display = ("name", "year_foundation",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class PilotAdmin(admin.ModelAdmin):
    list_display = ["name", "surname",]

admin.site.register(Pilot, PilotAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Balloon)
admin.site.register(Flight)

"""


