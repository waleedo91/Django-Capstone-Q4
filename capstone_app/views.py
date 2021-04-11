from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Avg
import json

# from .models import Game, GameGenre, GameReview, Player

import requests

from .models import Game
# Create your views here.

def index(request):
    url = 'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&metacritic=%2295,100%22&page_size=40'
    response = requests.request("GET", url)
    resp = response.json()
    return render(request, 'index.html', {'game': resp})
