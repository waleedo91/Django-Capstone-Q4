from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import requests


# API must be set in env and settings
from capstone_django.settings import API

# Imported from capstone_app
from .forms import GameReviewForm, SignupForm, LoginForm
from .models import Game, GameGenre, Player, GameReview


"""Created for homepage to display popular games"""


def index(request):
    url = f'https://api.rawg.io/api/games?key={API}'
    response = requests.request("GET", url)
    resp = response.json()
    player = User.objects.all()
    return render(request, 'index.html', {
        'game': resp,
        'player': player,
        })


"""Detailed view for a specific game via id"""


def gameview(request, game_id):
    url = f'https://api.rawg.io/api/games/{ game_id }?key={API}'
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'game.html', {'game': resp})





""" ReviewsView should show all reviews """


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


'''View created to display User profile page'''


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


"""View to create a review on specific game by User. Login required"""


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


# Game Genre View
"""This is a simple about us page"""
def aboutus(request):
    html = "aboutus.html"
    return render(request, html)
