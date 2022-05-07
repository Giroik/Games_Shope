from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    price=models.DecimalField(max_digits=9,decimal_places=2)
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    img=models.ImageField(blank=True)
    def get_absolut_url(self):
        return reverse('game_detail', args=[self.slug])

    def __str__(self):
        return f'{self.title}'




