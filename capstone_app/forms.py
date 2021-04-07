from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Game, GameGenre, GameReview, Player


class SignupForm(UserCreationForm):
    class Meta:
        model = Player
        fields = (
            'user',
            'name',
            'favorite_games'
        )


class UserChangeForm(UserChangeForm):
    class Meta:
        model = Player
        fields = (
            'name',
            'favorite_games'
        )
