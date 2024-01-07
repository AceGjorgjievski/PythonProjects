from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Author(models.Model):
    name_surname = models.CharField(max_length=255)
    year_birth = models.IntegerField()
    country = models.CharField(max_length=255)
    biography = models.TextField()

    def __str__(self):
        return f"{self.name_surname}"


class PublishHouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    country = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} -- {self.country}"

class Book(models.Model):
    isbn = models.CharField(max_length=17)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_house = models.ForeignKey(PublishHouse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.isbn} -- {self.title}"


class PublicationAuthor(models.Model):
    publishing_house = models.ForeignKey(PublishHouse, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)