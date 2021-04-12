from django.http.response import Http404
from django.shortcuts import render
from .models import Game
import requests
import json

# from .models import Game, GameGenre, GameReview, Player

import requests
# Create your views here.
# gets game id from url and returns game information
def gameview(request, game_id):
    url = f'https://api.rawg.io/api/games/{ game_id }?key=1d0a743d255d48418ee551a3eb563813'
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'game.html', {'game': resp})
