from django.shortcuts import render
from .models import Game

# Create your views here.
def gameview(request, game_id):
    # game id = api_req(id)
    # check to see if game data exists
    game = Game.objects.get(id=game_id)
    return render(request, 'game.html', {'game': game})
    # else
    # Search API for game and add to database

