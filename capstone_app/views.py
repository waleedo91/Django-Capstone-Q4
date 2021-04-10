from django.http.response import Http404
from django.shortcuts import render
from .models import Game
import requests
import json

# Create your views here.
gamesList = dict()
# exit_flag = False
def create_games(request):
    url = 'https://api.rawg.io/api/platforms/lists/parents?key=1d0a743d255d48418ee551a3eb563813&page_size=100&platforms=18&language="eng"'
    playstation_4_games = 'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&dates=2019-01-01,2019-12-31&ordering=-added&language=en'
    response = requests.request("GET", playstation_4_games)
    res_dict = response.json()
    print(res_dict)
    return render(request, 'index.html', {'dict': res_dict})

def gameview(request, game_id):
    game_id = 21
    url = f'https://api.rawg.io/api/games/{ game_id }?key=1d0a743d255d48418ee551a3eb563813'
    game = requests.request("GET", url)
    resp = game.json()
    print(resp)
    return render(request, 'game.html', {'game': resp})

def games(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})

