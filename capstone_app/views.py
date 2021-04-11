from django.http.response import Http404
from django.shortcuts import render
from .models import Game
import requests
import json

# Create your views here.
# gets game id from url and returns game information
def homeview(request):
    return render(request, 'index.html', {})

def gameview(request, game_id):
    url = f'https://api.rawg.io/api/games/{ game_id }?key=1d0a743d255d48418ee551a3eb563813'
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'game.html', {'game': resp})

def searchview(request):
    search_results = request.GET('query')
    url = f'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&page_size=1000&search="{ search_results }"'
    results = requests.request("GET", url)
    readable_results = results.json()
    return render(request, 'search_page.html', {'results', readable_results})

