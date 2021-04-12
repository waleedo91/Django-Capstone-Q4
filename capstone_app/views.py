from django.http.response import Http404
import requests
from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Game, GameGenre, Player, GameReview
from django.views.generic import View
# from django.contrib.auth.decorators import login_required
from .forms import GameReviewForm, SignupForm


# from .models import Game, GameGenre, GameReview, Player

# Create your views here.
# gets game id from url and returns game information
def gameview(request, game_id):
    url = f'https://api.rawg.io/api/games/{ game_id }?key=1d0a743d255d48418ee551a3eb563813'
    game = requests.request("GET", url)
    resp = game.json()
    return render(request, 'game.html', {'game': resp})

def add_review(request):
    if request.method == 'POST':
        form = GameReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GameReview.objects.create(
                game=data['game'],
                rating_score=data['rating_score'],
                body = data['body']
            )
            return HttpResponseRedirect('/')
        
    form = GameReviewForm()
    return render(request, 'newreview.html', {'form': form})

class SignUp(View):

    def get(self, request):
        form = SignupForm
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        # if request.method == 'POST':
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
