from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Avg

# from .models import Game, GameGenre, GameReview, Player

import requests
# Create your views here.


def index(request):
    url = 'https://rawg-video-games-database.p.rapidapi.com/games'

    headers = {
        'x-rapidapi-key': "9bb829cd6cmshaf5a1d3c29abfd5p1e73d1jsnaa321c9a0d6e",
        'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    game_data = response.json()
    return render(request, 'index.html', {
        'game': game_data,
    })
