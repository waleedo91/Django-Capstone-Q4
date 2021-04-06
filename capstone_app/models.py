from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.utils import timezone

# Create your models here.


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
