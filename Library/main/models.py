from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Genre(models.Model):

    genre = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self) -> str:
        return self.genre

class Book(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    cover = CloudinaryField('images')
    description = models.TextField(max_length=50000, null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='genres', blank=True)
    body = models.TextField(null=True, blank=True, default="Book")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-date_added']
