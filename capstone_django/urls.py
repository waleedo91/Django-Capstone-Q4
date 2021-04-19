"""capstone_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from capstone_app import views
# Added the Player and Index urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('game/<int:id>/', views.gameview, name='gameview'),
    path('search/', views.searchview, name='search_result'),
    # path('create_gameslist/', views.gameslist, name='gameslist'),
    path('games_list/', views.get_games, name = "get_games"),
    path('add_review/<int:game_id>/', views.add_review, name='add_review'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view),
    path('player/<int:user_id>/', views.playerView, name="playerview"),
    path('favgame/<int:id>/', views.favorites_view),
    path('reviews/', views.ReviewsView.as_view(), name='review'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('', include('capstone_app.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
# handler404 = 'capstone_app.views.handler404'
