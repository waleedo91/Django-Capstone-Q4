from os import name
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import response
from django.http.request import RAISE_ERROR
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.urls import NoReverseMatch
import requests


# API must be set in env and settings
from capstone_django.settings import API

# Imported from capstone_app
from .forms import GameReviewForm, SignupForm, LoginForm
from .models import Game, Player, GameReview
from django.views.generic import View

"""Created for homepage to display popular games"""

genres = [
        'action',
        'indie',
        'role-playing-games-rpg',
        'massively-multiplayer',
    ]

def gamegenres(genre):
    for g in genres:
        if g == genre:
            url = f'https://api.rawg.io/api/games?&genres={ g }&page_size=40&key={API}'
            # print(url)
            response = requests.request('GET', url)
            resp = response.json()
            # print(response.json())
    return resp

def index(request):
    url = f'https://api.rawg.io/api/games?key={API}&metacritic="95,100"&page_size=40&ordering=-metacritic&dates=2000,2021'
    response = requests.request("GET", url)
    resp = response.json()
    player = User.objects.all()
    action = gamegenres('action')
    multiplayer = gamegenres('massively-multiplayer')
    rpg = gamegenres('role-playing-games-rpg')
    indie = gamegenres('indie')
    return render(request, 'index.html', {
        'games': resp,
        'player': player,
        'action': action,
        'multiplayer': multiplayer,
        'rpg': rpg,
        'indie': indie
        })


def genre_view(request):
    url = f'https://api.rawg.io/api/games?key={API}'


"""Detailed view for a specific game via id"""
from operator import itemgetter

def gameview(request, game_id):
    # url = f'https://api.rawg.io/api/games/{ game_id }?key={API}'
    # game = requests.request("GET", url)
    # resp = game.json()
    game = Game.objects.get(game_id=game_id)
    review = GameReview.objects.filter(game_id=game.id)
    print(review)
    return render(request, 'game.html', {
        # 'game': resp,
        'game':game,
        'review': review,
        })


"""View created to display Search Results"""
def searchview(request):
    search_results = request.POST.get('query')
    url = f'https://api.rawg.io/api/games?key={API}&page_size=40&search="{ search_results }"'
    game = requests.request("GET", url)
    resp = game.json()
    print(resp)
    return render(request, 'search_page.html', {'results': resp})


"""View created to display User profile page"""
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


"""Favorite games for your favorite games"""
def favorites(request, game_id, user_id):
    player = Player.objects.get(id=user_id)
    game = Game.objects.get(game_id=game_id)
    if game not in player.favorite_games.all():
        player.favorite_games.add(game_id=game_id)
        player.save()
        print(player.favorite_games.all())
    else:
        for g in player.favorite_games.all():
            player.favorite_games.remove(game_id=game_id)
            player.save()
        print(player.favorite_games.all())
    return render(request, 'game.html')


"""View created to show all reviews """

# https://api.rawg.io/api/games/{game_id}/reddit?key={API}

class ReviewsView(View):
    def get(self, request):
        reviews = GameReview.objects.all().order_by('-created_at')
        html = 'Reviews.html'
        return render(
            request,
            html,
            {"reviews": reviews}
        )


# '''function to create a review for a game'''

def add_review(request, game_id):
    if request.user.is_authenticated:
        game = Game.objects.get(game_id=game_id)
        if request.method == "POST":
            form = GameReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.title = request.POST["title"]
                data.body = request.POST['body']
                data.rating_score=request.POST['rating_score']
                data.user = request.user
                data.game = game
                data.save()
                return redirect(f"/game/{game_id}/")
        else:
            print(game)
            form = GameReviewForm()
        return render(request, 'newreview.html', {'form': form})
    else:
        return redirect('login')



'''Creates the game and floods into the database'''




class PlayerView(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        player = Player.objects.filter(user=user)
        return render(
            request,
            'player.html',
            {
                'user': user,
                'player': player,
            }
        )



def handler404(request, exception):
    response = render(request, '404.html')
    response.status = 404
    return response


"""Create a new profile for user"""

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            Player.objects.create(
                name=data['name'],
                user=new_user
            )
        login(request, new_user)
        return HttpResponseRedirect(reverse('home'))

    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                player = authenticate(
                    request, username=data['username'], password=data['password'])
                if player:
                    login(request, player)
                    return HttpResponseRedirect(request.GET.get('next', '/'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


"""This is a simple about us page"""
def aboutus(request):
    html = "aboutus.html"
    return render(request, html)



'''DO NOT USE!!! This is used for adding games to Database
But leave alone in case we need to add more to database.'''

@staff_member_required
def get_games(request):
    # game_id is for when you would like to add and specific id.
    game_id = []
    all_games = {}
    for i in game_id:
        url = f'https://api.rawg.io/api/games/{i}?key={API}'
        print(url)
        response = requests.get(url)
        if response.status_code == 404:
            KeyError('Does not exist')
        else:
            i = response.json()
            # games = data['ratings']
            # print(games)
            Game.objects.create(
                name = i['name'],
                esrb_rating = i['esrb_rating'],
                rating = i['rating'],
                metacritic = i['metacritic'],
                description_raw=i['description_raw'],
                genres=i['genres'],
                slug = i['slug'],
                background_image = i['background_image'],
                game_id=i['id'],
                released=i['released']
            )
            if not Game.objects.filter(name=i['name']).exists():
                print(i)
                i.save()
                all_games = Game.objects.all()



    return render (request, 'games_list.html', { "all_games":
    all_games} )
