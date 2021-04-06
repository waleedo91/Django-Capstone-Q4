from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class GameGenre(models.Model):
    ACTION = 'Action'
    INDIE = 'Indie'
    ADVENTURE = 'Adventure'
    RPG = 'Rpg'
    STRATEGY = 'Strategy'
    SHOOTER = 'Shooter'
    CASUAL = 'Casual'
    SIMULATION = 'Simulation'
    PUZZLE = 'Puzzle'
    ARCADE = 'Arcade'
    PLATFORMER = 'Platformer'
    RACING = 'Racing'
    MASSIVELY_MULTIPLAYER = 'Massively Multiplayer'
    SPORTS = 'Sports'
    FIGHTING = 'Fighting'
    FAMILY = 'Family'
    BOARD_GAMES = 'Board Games'
    EDUCATIONAL = 'Educational'
    CARD = 'Card'

    GENRE_CHOICES = [
        (ACTION, 'action'),
        (INDIE, 'indie'),
        (ADVENTURE, 'adventure'),
        (RPG, 'rpg'),
        (STRATEGY, 'strategy'),
        (SHOOTER, 'shooter'),
        (CASUAL, 'casual'),
        (SIMULATION, 'simulation'),
        (PUZZLE, 'puzzle'),
        (ARCADE, 'arcade'),
        (PLATFORMER, 'platformer'),
        (RACING, 'racing'),
        (MASSIVELY_MULTIPLAYER, 'massively_multiplayer'),
        (SPORTS, 'sports'),
        (FIGHTING, 'fighting'),
        (FAMILY, 'family'),
        (BOARD_GAMES, 'board_games'),
        (EDUCATIONAL, 'educational'),
        (CARD, 'card')
    ]

    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)

    def __str__(self):
        return self.genre


class Game(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(GameGenre, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateField(auto_now_add=True)
    total_rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    favorite_games = models.ForeignKey(Game, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class GameReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    rating_score = models.IntegerField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.game} | {self.rating_score}'
