from django.urls import NoReverseMatch
import requests
from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Game, GameGenre, Player, GameReview
from django.views.generic import View
from django.http import HttpResponseNotFound
from dal import autocomplete

# from django.contrib.auth.decorators import login_required

# from .models import Game, GameGenre, GameReview, Player

# Create your views here.
# gets game id from url and returns game information
def homeview(request):
    return render(request, 'index.html', {})

def gameview(request, game_id):
    url = f'https://api.rawg.io/api/games/{ game_id }?key=1d0a743d255d48418ee551a3eb563813'
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'game.html', {'game': resp})


page = 773
def gameslist(request):
    global page
    exit_flag = False
    last_page = 13361
    def createGames(url):
        global page
        # last_page = 2
        if page > last_page:
            exit_flag = True
        # url = f'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&page={ page }&page_size=40'
        response = requests.request('GET', f'{ url }&page={ page }')
        resp = response.json()
        print(f'{ url }&page={ page }')
        for item in resp['results']:
            if item['name'] not in Game.objects.all():
                Game.objects.create(name=item['name'], game_id=item['id'])
        
        page = page + 1
        print(page)
        return page

    while not exit_flag:
        try:
            url = f'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&page_size=40'
            createGames(url)
        except NoReverseMatch:
            exit_flag = True
            print('finished loading games')

    return render(request, 'index.html', {})


class GameAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Filter out results depending on the visitor
        if not self.request.user.is_authenticated:
            return Game.objects.none()
        
        qs = Game.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        
        return qs


def searchview(request):
    search_results = request.POST.get('query')
    url = f'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&page_size=1000&search="{ search_results }"'
    game = requests.request("GET", url)
    resp = game.json()
    print(resp)
    return render(request, 'search_page.html', {'results': resp})


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
