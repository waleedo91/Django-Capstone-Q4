from django import forms
from django.forms.widgets import Textarea

from .models import GameGenre, Game, Player, GameReview

'''Going to give the game variable a test to make sure we are able to choose from listed games and choose from that list.

-Waleed'''


class GameReviewForm(forms.Form):
    game = forms.ModelsChoiceField(queryset=Game.objects.all())
    rating_score = forms.DecimalField(max_value=3, decimal_places=2)
    body = forms.CharField(widget=Textarea)
