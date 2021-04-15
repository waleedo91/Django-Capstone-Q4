from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import requests


# API must be set in env and settings
from capstone_django.settings import API

# Imported from capstone_app
from .forms import GameReviewForm, SignupForm, GameForm
from .models import Game, GameGenre, Player, GameReview
from django.views.generic import View

"""Created for homepage to display popular games"""
def index(request):
    form = GameForm
    url = f'https://api.rawg.io/api/games?key={API}&metacritic=%60,100%22&page_size=40&dates=2015-01-01,2020-12-31&ordering=-metacritic'
    response = requests.request("GET", url)
    resp = response.json()
    player = User.objects.all()
    return render(request, 'index.html', {
        'game': resp,
        'player': player,
        })


"""Detailed view for a specific game via id"""


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


# page = 773
# def gameslist(request):
#     global page
#     exit_flag = False
#     last_page = 13361
#     def createGames(url):
#         global page
#         # last_page = 2
#         if page > last_page:
#             exit_flag = True
#         # url = f'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&page={ page }&page_size=40'
#         response = requests.request('GET', f'{ url }&page={ page }')
#         resp = response.json()
#         print(f'{ url }&page={ page }')
#         for item in resp['results']:
#             if item['name'] not in Game.objects.all():
#                 Game.objects.create(name=item['name'], game_id=item['id'])
        
#         page = page + 1
#         print(page)
#         return page

#     while not exit_flag:
#         try:
#             url = f'https://api.rawg.io/api/games?key=1d0a743d255d48418ee551a3eb563813&page_size=40'
#             createGames(url)
#         except NoReverseMatch:
#             exit_flag = True
#             print('finished loading games')

#     return render(request, 'index.html', {})


# class GameAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         # # Filter out results depending on the visitor
#         # if not self.request.user.is_authenticated:
#         #     return Game.objects.none()
        
#         qs = Game.objects.all()

#         if self.q:
#             qs = qs.filter(name__istartswith=self.q)
        
        
#         return qs
    # def get_result_label(self, item):
    #     return item.full_name
        

    # def get_selected_result_label(self, item):
    #     return item.short_name


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
