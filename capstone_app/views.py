from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import requests
import re

# API must be set in env and settings
from capstone_django.settings import API

# Imported from capstone_app
from .forms import GameReviewForm, SignupForm, LoginForm, PlayerForm
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
            response = requests.request('GET', url)
            resp = response.json()
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


'''View to add favorite games to player profile'''
@login_required
def favorites_view(request, id):
    game = get_object_or_404(Game, game_id=id)
    if game.favorite_games.filter(id=request.user.id).exists():
        game.favorite_games.remove(request.user)
    else:
        game.favorite_games.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


'''To view the favorite on page'''

def favorite_games_list(request):
    user = request.user.id
    favorite = user.favorite.all()
    return render(request, 'favorite_game.html', {'favorite': favorite})


'''Cleans <html> tags to normal text'''

def cleanhtml(string):
    cleanr = re.compile('<.*?>')
    game_information = re.sub(cleanr, '', string)
    return game_information


"""Detailed view for a specific game via id"""

def gameview(request, id):
    game = Game.objects.get(game_id=id)
    review = GameReview.objects.filter(game_id=game.id)
    reddit_reviews_url = f'https://api.rawg.io/api/games/{ id }/reddit?key={API}'
    reddit_reviews_request = requests.request("GET", reddit_reviews_url)
    reddit_reviews = reddit_reviews_request.json()

    is_favorite = False
    if game.favorite_games.filter(id=request.user.id).exists():
        is_favorite = True
    reddit_reviews_results = reddit_reviews['results']
    for r in reddit_reviews_results:
        cleaned = cleanhtml(r['text'])
        r['text'] = cleaned

    return render(request, 'game.html', {
        # 'game': resp,
        'game':game,
        'review': review,
        'reddit_reviews': reddit_reviews,
        'is_favorite': is_favorite
        })


"""View created to display Search Results"""


def searchview(request):
    search_results = request.POST.get('query')
    url = f'https://api.rawg.io/api/games?key={API}&page_size=40&search="{ search_results }"'
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'search_page.html', {'results': resp})


"""View created to display User profile page"""


def playerView(request, user_id):
    user = User.objects.get(id=user_id)
    player = Player.objects.get(user=user)
    return render(request, 'player.html', {'player':player})


"""View created to show all reviews """

class ReviewsView(View):
    def get(self, request):
        reviews = GameReview.objects.all().order_by('-created_at')
        html = 'Reviews.html'
        return render(
            request,
            html,
            {"reviews": reviews}
        )



'''function to create a review for a game'''

def add_review(request, game_id):
    if request.user.is_authenticated:
        game = Game.objects.get(game_id=game_id)
        if request.method == "POST":
            form = GameReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.review = request.POST["review"]
                data.description = request.POST['description']
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


'''Handles error pages when not in production'''

def handler404(request, *args, **argv):
    return render(request, '404.html')


def handler500(request, *args, **argv):
    return render(request, '500.html')



"""Create a new profile for user"""

class SignUpView(View):
    def get(self, request):
        template_name = "generic_form.html"
        form = SignupForm()
        return render(request, template_name, {
            'form': form,
        })

    def post (self, request):
        if request.method == "POST":
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
            return redirect(reverse('home'))

'''Logs user in'''

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

'''Logs user out'''


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def edit_profile(request, id):
    player = Player.objects.get(id=id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        form.save()
        return HttpResponseRedirect(reverse('playerview', args=(id,)))
    form = PlayerForm(instance=player)
    return render(request, 'edit_profile.html', {'form': form})


"""This is a simple about us page"""

def aboutus(request):
    html = "aboutus.html"
    return render(request, html)



'''DO NOT USE!!! This is used for adding games to Database
But leave alone in case we need to add more to database.'''

@staff_member_required
def get_games(request):
    # game_id is for when you would like to add a specific id.
    game_id = [
       54531,
        58829
    ]
    all_games = {}
    for i in game_id:
        url = f'https://api.rawg.io/api/games/{i}?key={API}'
        print(url)
        response = requests.get(url)
        if response.status_code == 404:
            KeyError('Does not exist')
        else:
            i = response.json()
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
