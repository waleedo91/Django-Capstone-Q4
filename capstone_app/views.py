from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect
import requests

# API must be set in env and settings
from capstone_django.settings import API

# Imported from capstone_app
from .forms import GameReviewForm, SignupForm
from .models import Game, GameGenre, Player, GameReview
from django.views.generic import View

"""Created for homepage to display popular games"""
def index(request):
    url = f'https://api.rawg.io/api/games?key={API}&metacritic=%60,100%22&page_size=40&dates=2015-01-01,2020-12-31&ordering=-metacritic'
    response = requests.request("GET", url)
    resp = response.json()
    return render(request, 'index.html', {'game': resp,})


"""View created for a specific game via id"""
def gameview(request, game_id):
    url = f'https://api.rawg.io/api/games/{ game_id }?key={API}'
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'game.html', {'game': resp})


"""View created to display Search Results"""
def searchview(request):
    search_results = request.POST.get('query')
    url = f'https://api.rawg.io/api/games?key={API}&page_size=40&search="{ search_results }"'
    game = requests.request("GET", url)
    resp = game.json()
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


"""View created for a review on specific game"""
@login_required
def add_review(request):
    if request.method == 'POST':
        form = GameReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GameReview.objects.create(
                game=data['game'],
                rating_score=data['rating_score'],
                body=data['body']
            )
            return HttpResponseRedirect('/')

    form = GameReviewForm()
    return render(request, 'newreview.html', {'form': form})


"""View created a new user"""
class SignUp(View):

    def get(self, request):
        form = SignupForm
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = Player.objects.create(
                user=data['user'],
                password=data['password'],
                name=data['name'],
            )
            return render(request, 'index.html', {'user': new_user})

        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})


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
        # user=request.user,
        # game=request.game,
        # rating_score=request.rating_score,
        # body=request.body,
