from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.

'''Uncomment favorite_games once merged'''


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    # favorite_games = models.ForeignKey(Game, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


"""Uncomment game variable(model) once Game model is finished"""


class GameReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    rating_score = models.IntegerField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return f' | {self.rating_score}'
