from django import forms
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import GameGenre, Game, Player, GameReview
from dal import autocomplete

'''Going to give the game variable a test to make sure we are able to choose from listed games and choose from that list.

-Waleed'''


class GameReviewForm(forms.Form):
    game = forms.ModelsChoiceField(queryset=Game.objects.all())
    rating_score = forms.DecimalField(max_value=3, decimal_places=2)
    body = forms.CharField(widget=Textarea)


class SignupForm(UserCreationForm):
    class Meta:
        model = Player
        fields = (
            'user',
            'name',
            'favorite_games'
        )


class GameForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=Game.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='game-autocomplete',
            attrs={
                'data-placeholder': 'Enter a game...',
                # Only trigger autocomplete after three chars have been typed.
                'data-minimum-input-length': 3,
            })
    )
    
    class Meta:
        model = Game
        fields = ('name',)


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
