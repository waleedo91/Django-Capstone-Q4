from django.shortcuts import render, HttpResponseRedirect
from .models import GameReview, Player
from django.views import View
import requests
from .forms import GameReviewForm, SignupForm


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
