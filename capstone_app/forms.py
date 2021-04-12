from django import forms
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import GameGenre, Game, Player, GameReview

'''Going to give the game variable a test to make sure we are able to choose from listed games and choose from that list.

-Waleed'''


class GameReviewForm(forms.Form):
    game = forms.CharField(max_length=40)
    rating_score = forms.DecimalField(max_value=10, decimal_places=2)
    body = forms.CharField(max_length=100)


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


class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = (
            'name',
        )
