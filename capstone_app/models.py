import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50, null=True)
    game_id = models.IntegerField(default=None, null=False)
    genres = models.JSONField()
    released = models.CharField(max_length=100, null=True)
    description_raw = models.TextField(null=True)
    background_image = models.ImageField(upload_to='static/images')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    metacritic = models.IntegerField(default=None, null=True)
    esrb_rating = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.name} | {self.game_id}'


class Player(models.Model):
    # Create a platform choice for user. 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    about = models.TextField(null=True)
    favorite_games = models.CharField(max_length=100, null=True, blank=True)
    registration_date = models.DateField(default=django.utils.timezone.now)
    id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.name


class GameReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    rating_score = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user} | {self.game} | rating: {self.rating_score}'
