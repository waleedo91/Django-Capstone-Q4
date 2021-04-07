from django import forms
from django.forms.widgets import Textarea

from .models import GameGenre, Game, Player, GameReview


class GameReviewForm(forms.Form):
    game = forms.ModelsChoiceField(queryset=Game.objects.all())
    rating_score = forms.DecimalField(max_value=3, decimal_places=2)
    body = forms.CharField(widget=Textarea)
