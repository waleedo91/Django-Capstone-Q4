from django.shortcuts import render, reverse, HttpResponseRedirect
from capstone_app.models import Game, GameGenre, Player, GameReview
from django.contrib.auth.decorators import login_required

# Create your views here.
# Player View
def playerview(request, user_id):
    new_player = Player.objects.create(
        id=user_id,
    )
    return new_player

    # def user_detail(request, user_id):
    # requested_user = TwitterUser.objects.get(id=user_id)
    # return requested_user



# Game View

# Index View

# Signup View

# Game Genre View

# Game Review View