from django.shortcuts import render
import requests

from .models import Game
# Create your views here.


def index(request):
    game = Game.objects.all()
    return render(request, 'index.html', {
        'game': game
    })
