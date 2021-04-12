from django.http.response import Http404
import requests
from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Game, GameGenre, Player, GameReview
from django.views.generic import View
# from django.contrib.auth.decorators import login_required
from django.http import response
# Create your views here.


def index(request):
    url = 'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&metacritic=%2295,100%22&page_size=40'
    response = requests.request("GET", url)
    resp = response.json()
    return render(request, 'index.html', {'game': resp})


def gameview(request, game_id):
    url = f'https://api.rawg.io/api/games/{ game_id }?key=1d0a743d255d48418ee551a3eb563813'
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'game.html', {'game': resp})


''' Made the ReviewsView and the player view and they should be working'''

""" ReviewsView should show all reviews """
# Index View


class ReviewsView(View):
    def get(self, request):
        reviews = GameReview.objects.all().order_by('-created_at')
        html = 'Reviews.html'
        return render(
            request,
            html,
            {"reviews": reviews}
        )
        # user=request.user,
        # game=request.game,
        # rating_score=request.rating_score,
        # body=request.body,


'''Made the user show up on player htmlpage'''
# Player View


class PlayerView(View):
    def get(self, request, user_id):
        new_player = Player.objects.get(
            id=user_id
        )
        return render(
            request,
            'player.html',
            {'new_player': new_player}
        )

# Game View

# Signup View

# Game Genre View

# Game Review View
