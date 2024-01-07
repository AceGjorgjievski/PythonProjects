from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BlogPostUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    interests = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(BlogPostUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    files = models.FileField(upload_to="files/")
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    content = models.CharField(max_length=255)
    date_created = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(BlogPostUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"


class Block(models.Model):
    user_blocker = models.ForeignKey(BlogPostUser, on_delete=models.CASCADE, related_name="blocker")
    user_blocked = models.ForeignKey(BlogPostUser, on_delete=models.CASCADE, related_name="blocked")

    def __str__(self):
        return f"{self.user_blocker} --> {self.user_blocked}"