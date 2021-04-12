from django.contrib import admin
from .models import Player, GameReview, GameGenre, Game

class gameAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'name')

# Register your models here.
admin.site.register(Player)
admin.site.register(GameReview)
admin.site.register(GameGenre)
admin.site.register(Game, gameAdmin)
