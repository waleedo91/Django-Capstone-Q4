from django.http.response import Http404
from django.shortcuts import render
from .models import Game
import requests

# Create your views here.
max_num = 5
gamesList = dict()
exit_flag = False
def create_games(request):
    i = 257
    while not exit_flag:
        try:
            url = f"https://rawg-video-games-database.p.rapidapi.com/games/{ i }"
            headers = {
                'x-rapidapi-key': "4329ef7408msh53be98e03ed8801p11ea0djsn9d388763b4fa",
                'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers)
            resp = response.json()
            Game.objects.create(name=resp['name'], game_id=resp['id'])
            i += 1
            print('game added')
        except ConnectionRefusedError:
            break

def gameview(request, game_id):
    game = Game.objects.get(game_id=game_id)
    return render(request, 'game.html', {'game': game})

def games(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})

