from django import forms
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.widgets import PasswordInput

from .models import GameGenre, Game, Player, GameReview

'''Going to give the game variable a test to make sure we are able to choose from listed games and choose from that list.

-Waleed'''


class GameReviewForm(forms.ModelForm):
    
    class Meta:
        model = GameReview
        fields = ('game', 'rating_score', 'body')


class SignupForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    name = forms.CharField(max_length=100)



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
