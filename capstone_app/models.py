import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class GameGenre(models.Model):
    GENRE_CHOICES = [
        ('ACTION', 'action'),
        ('INDIE', 'indie'),
        ('ADVENTURE', 'adventure'),
        ('RPG', 'rpg'),
        ('STRATEGY', 'strategy'),
        ('SHOOTER', 'shooter'),
        ('CASUAL', 'casual'),
        ('SIMULATION', 'simulation'),
        ('PUZZLE', 'puzzle'),
        ('ARCADE', 'arcade'),
        ('PLATFORMER', 'platformer'),
        ('RACING', 'racing'),
        ('MASSIVELY_MULTIPLAYER', 'massively_multiplayer'),
        ('SPORTS', 'sports'),
        ('FIGHTING', 'fighting'),
        ('FAMILY', 'family'),
        ('BOARD_GAMES', 'board_games'),
        ('EDUCATIONAL', 'educational'),
        ('CARD', 'card')
    ]

    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)

    def __str__(self):
        return self.genre


class Game(models.Model):
    name = models.CharField(max_length=50)
    game_id = models.IntegerField(default=None)

    def __str__(self):
        return self.name


class Player(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null=False, blank=False)
    favorite_games = models.CharField(max_length=100, null=True, blank=True)
    registration_date = models.DateField(default=django.utils.timezone.now)


    def __str__(self):
        return self.name


class GameReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    game = models.CharField(max_length=50)
    rating_score = models.IntegerField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.game} | rating: {self.rating_score}'
