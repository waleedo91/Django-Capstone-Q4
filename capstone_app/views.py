from django.http import response
from django.shortcuts import render
import requests
from capstone_django.settings import DATABASES

from .models import Game
# Create your views here.

# url = f"https://api.rawg.io/api/games?key={{DATABASES.API}}"


def index(request):
    url = "https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&metacritic=%2295,100%22&page_size=20"
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'index.html', {
        'games': resp
    })


