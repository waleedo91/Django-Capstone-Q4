from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Game, GameGenre, GameReview, Player
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
        "name",
        "username",
        "password1",
        "password2",
        ]


class UpdateForm(UserChangeForm):
    class Meta:
        model = Player
        fields = (
            'name',
            'favorite_games'
        )


class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = (
            'name',
        )
