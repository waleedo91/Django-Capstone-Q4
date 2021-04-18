from django.contrib import admin
from .models import Player, GameReview, Game

# class gameAdmin(admin.ModelAdmin):
#     list_display = ('game_id', 'game')

# Register your models here.
admin.site.register(Player)
admin.site.register(GameReview)
admin.site.register(Game)
