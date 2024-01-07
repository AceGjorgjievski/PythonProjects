

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "polls2"

urlpatterns = [
    # /polls2/
    path('', views.index, name="index"),
]
