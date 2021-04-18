from django import forms
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.widgets import PasswordInput

from .models import Game, Player, GameReview


'''Going to give the game variable a test to make sure we are able to choose from listed games and choose from that list.

-Waleed'''


class GameReviewForm(forms.ModelForm):

    class Meta:
        model = GameReview
        fields = ('review', 'rating_score', 'description')


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


# class AddGameForm(forms.ModelForm):
#     class Meta:
#         model = Game
#         fields = (
#             'game',
#         )
