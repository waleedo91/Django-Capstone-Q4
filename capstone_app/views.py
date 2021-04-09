from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Game, GameGenre, Player, GameReview
# from django.contrib.auth.decorators import login_required

# Create your views here.


''' Made the Indexview and the player view and they should be working'''
# Index View
def indexview(request):
    reviews = GameReview.objects.all().order_by('-created_at')
    html = 'index.html'
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
def playerview(request, user_id):
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