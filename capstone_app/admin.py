from django.contrib import admin
from .models import Player, GameReview, GameGenre, Game

# Register your models here.
admin.site.register(Player)
admin.site.register(GameReview)
admin.site.register(GameGenre)
admin.site.register(Game)
